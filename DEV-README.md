# Anthropic Documentation Scraper

Automatically downloads and monitors [Anthropic's documentation](https://docs.claude.com) for changes. Downloads pre-generated markdown files directly from the docs site and maintains a local mirror.

## Features

- **Direct .md downloads** - Fetches pre-generated markdown files for better quality
- **Change detection** - MD5 hashing tracks updates and only downloads changed files
- **Auto fallback** - Falls back to HTML parsing for pages without .md endpoints
- **Monitoring mode** - Continuous monitoring with configurable check intervals
- **Local mirror** - Maintains the same directory structure as the website

## Quick Start

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run once (download all docs and exit)
python3 scraper.py --once

# Continuous monitoring (default: checks every 60 minutes)
python3 scraper.py
```

## Configuration

Edit `config.json`:

```json
{
  "output_directory": "./anthropic_docs",
  "check_interval_minutes": 60,
  "starting_urls": ["https://docs.claude.com/en/docs/welcome"],
  "max_depth": 5,
  "delay_seconds": 0.5
}
```

## Output

Downloaded docs are saved to `anthropic_docs/` with metadata tracking in `metadata.json`:

```
anthropic_docs/
├── metadata.json          # Change tracking (hashes, timestamps)
└── docs/
    ├── welcome.md
    ├── intro.md
    └── [mirrors website structure]
```

## How It Works

1. Crawls docs.claude.com starting from configured URLs
2. Attempts to fetch `.md` file for each page (e.g., `/docs/quickstart.md`)
3. Falls back to HTML parsing if no `.md` endpoint exists
4. Compares MD5 hash to detect changes before writing
5. Updates metadata with timestamps and file info

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- lxml
- schedule

## License

MIT
