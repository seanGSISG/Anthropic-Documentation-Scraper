"""
Enhanced Anthropic Documentation Scraper with better markdown conversion
"""

import os
import time
import hashlib
import json
import logging
from pathlib import Path
from typing import Set, Dict, Optional
from datetime import datetime
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import schedule

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class AnthropicDocsScraperEnhanced:
    """Enhanced scraper with better markdown extraction."""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize the scraper with configuration."""
        self.config = self.load_config(config_path)
        self.base_url = "https://docs.claude.com"
        self.docs_dir = Path(self.config.get("output_directory", "./anthropic_docs"))
        self.metadata_file = self.docs_dir / "metadata.json"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AnthropicDocsMonitor/1.0'
        })

        # Create output directory
        self.docs_dir.mkdir(parents=True, exist_ok=True)
        
        # Load or initialize metadata
        self.metadata = self.load_metadata()
    
    def load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        else:
            # Default configuration
            default_config = {
                "output_directory": "./anthropic_docs",
                "check_interval_minutes": 60,
                "starting_urls": [
                    "https://docs.claude.com/en/docs/welcome"
                ],
                "max_depth": 5,
                "delay_seconds": 0.5
            }
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=2)
            logger.info(f"Created default config file: {config_path}")
            return default_config
    
    def load_metadata(self) -> Dict:
        """Load metadata about downloaded files."""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_metadata(self):
        """Save metadata to disk."""
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)
    
    def calculate_hash(self, content: str) -> str:
        """Calculate MD5 hash of content."""
        return hashlib.md5(content.encode('utf-8')).hexdigest()
    
    def normalize_url(self, url: str) -> str:
        """Normalize URL by removing fragments and trailing slashes."""
        parsed = urlparse(url)
        normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path.rstrip('/')}"
        return normalized
    
    def discover_all_docs(self) -> Set[str]:
        """Discover all documentation URLs by crawling the site."""
        discovered_urls = set()
        to_visit = [(url, 0) for url in self.config.get("starting_urls", [])]
        visited = set()
        max_depth = self.config.get("max_depth", 5)
        
        logger.info("Starting documentation discovery...")
        
        while to_visit:
            url, depth = to_visit.pop(0)
            url = self.normalize_url(url)
            
            if url in visited or depth > max_depth:
                continue
            
            visited.add(url)
            
            # Only process docs.claude.com URLs
            if not url.startswith(self.base_url):
                continue
            
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                
                # Check if it's a documentation page
                if '/docs/' in url or '/release-notes/' in url:
                    discovered_urls.add(url)
                    logger.info(f"Found: {url}")

                # Parse HTML to find more links
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find ALL links (not just nav elements) for better coverage
                links = soup.find_all('a', href=True)

                for link in links:
                    href = link['href']
                    absolute_url = urljoin(url, href)
                    absolute_url = self.normalize_url(absolute_url)

                    # Follow docs and release-notes links
                    if ('/docs/' in absolute_url or '/release-notes/' in absolute_url) and absolute_url.startswith(self.base_url):
                        if absolute_url not in visited:
                            to_visit.append((absolute_url, depth + 1))
                
                # Be polite - don't hammer the server
                time.sleep(self.config.get("delay_seconds", 0.5))
                
            except Exception as e:
                logger.error(f"Error processing {url}: {e}")
        
        logger.info(f"Discovery complete. Found {len(discovered_urls)} documentation pages.")
        return discovered_urls
    
    def extract_markdown_content(self, url: str) -> Optional[str]:
        """Fetch pre-generated markdown file directly from .md endpoint.
        Falls back to HTML parsing if .md endpoint is not available."""
        try:
            # First, try to fetch the pre-generated .md file
            md_url = url if url.endswith('.md') else f"{url}.md"

            response = self.session.get(md_url, timeout=10)

            if response.status_code == 404:
                # Fallback: .md endpoint not available, try HTML page
                logger.warning(f"No .md endpoint for {url}, falling back to HTML parsing")
                return self._extract_from_html(url)

            response.raise_for_status()

            # The markdown content is already pre-generated
            markdown = response.text

            # Add metadata header
            header = f"Source: {url}\n"
            header += f"Last fetched: {datetime.now().isoformat()}\n\n"
            header += "---\n\n"

            return header + markdown.strip()

        except Exception as e:
            logger.error(f"Error fetching content from {url}: {e}")
            return None

    def _extract_from_html(self, url: str) -> Optional[str]:
        """Fallback method: Extract content from HTML page when .md is not available."""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Try to find the main content area
            content = None
            for selector in [
                {'name': 'article'},
                {'name': 'main'},
                {'name': 'div', 'class': 'content'},
            ]:
                content = soup.find(**selector)
                if content:
                    break

            if not content:
                content = soup.find('body')

            if content:
                # Remove unwanted elements
                for element in content.find_all(['script', 'style', 'nav', 'footer', 'header']):
                    element.decompose()

                # Simple HTML to text conversion
                text = content.get_text(separator='\n', strip=True)

                # Add metadata header
                header = f"Source: {url}\n"
                header += f"Last fetched: {datetime.now().isoformat()}\n"
                header += f"Note: Extracted from HTML (no .md endpoint available)\n\n"
                header += "---\n\n"

                return header + text

            return None

        except Exception as e:
            logger.error(f"Error extracting HTML from {url}: {e}")
            return None
    
    def url_to_filepath(self, url: str) -> Path:
        """Convert URL to local filepath."""
        parsed = urlparse(url)
        path = parsed.path.strip('/')
        
        # Remove /en/ prefix if present
        if path.startswith('en/'):
            path = path[3:]
        
        # Handle root or empty paths
        if not path or path == 'docs':
            path = 'docs/index'
        
        # Ensure .md extension
        if not path.endswith('.md'):
            path += '.md'
        
        return self.docs_dir / path
    
    def download_document(self, url: str) -> bool:
        """Download a single document and check for changes."""
        content = self.extract_markdown_content(url)
        
        if not content:
            return False
        
        filepath = self.url_to_filepath(url)
        content_hash = self.calculate_hash(content)
        
        # Check if file has changed
        file_existed = filepath.exists()
        old_hash = self.metadata.get(url, {}).get('hash')
        
        if old_hash == content_hash:
            logger.debug(f"No changes detected: {url}")
            # Update last checked time even if no changes
            self.metadata[url]['last_checked'] = datetime.now().isoformat()
            return False
        
        # Create directory structure
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Write content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Update metadata
        self.metadata[url] = {
            'hash': content_hash,
            'last_updated': datetime.now().isoformat(),
            'last_checked': datetime.now().isoformat(),
            'filepath': str(filepath.relative_to(self.docs_dir)),
            'size_bytes': len(content.encode('utf-8'))
        }
        
        if file_existed:
            logger.info(f"✓ Updated: {url}")
        else:
            logger.info(f"✓ Downloaded: {url}")
        
        return True
    
    def scrape_all(self):
        """Scrape all documentation."""
        logger.info("=" * 80)
        logger.info(f"Starting scrape at {datetime.now().isoformat()}")
        logger.info("=" * 80)
        
        # Discover all documentation URLs
        urls = self.discover_all_docs()
        
        if not urls:
            logger.warning("No documentation URLs found. Check your starting URLs.")
            return
        
        # Download each document
        changes_detected = 0
        errors = 0
        
        for i, url in enumerate(urls, 1):
            logger.info(f"Processing ({i}/{len(urls)}): {url}")
            try:
                if self.download_document(url):
                    changes_detected += 1
                time.sleep(self.config.get("delay_seconds", 0.5))
            except Exception as e:
                logger.error(f"Failed to process {url}: {e}")
                errors += 1
        
        # Save metadata
        self.save_metadata()
        
        logger.info("=" * 80)
        logger.info(f"Scrape complete:")
        logger.info(f"  - Total documents: {len(urls)}")
        logger.info(f"  - Changes detected: {changes_detected}")
        logger.info(f"  - Errors: {errors}")
        logger.info("=" * 80)
    
    def start_monitoring(self):
        """Start the monitoring loop."""
        interval = self.config.get("check_interval_minutes", 60)
        
        logger.info(f"Starting monitoring with {interval} minute interval")
        logger.info("Press Ctrl+C to stop")
        
        # Run immediately on start
        self.scrape_all()
        
        # Schedule periodic runs
        schedule.every(interval).minutes.do(self.scrape_all)
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            logger.info("\nMonitoring stopped by user")


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Anthropic Documentation Scraper (Enhanced)')
    parser.add_argument('--config', default='config.json', help='Configuration file path')
    parser.add_argument('--once', action='store_true', help='Run once and exit (no monitoring)')
    
    args = parser.parse_args()
    
    scraper = AnthropicDocsScraperEnhanced(config_path=args.config)
    
    if args.once:
        scraper.scrape_all()
    else:
        scraper.start_monitoring()


if __name__ == "__main__":
    main()
