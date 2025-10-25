#!/usr/bin/env python3
"""
Generate README statistics from metadata.json
Updates README.md with recent changes and stats
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

def load_metadata() -> Dict:
    """Load metadata.json"""
    metadata_path = Path("anthropic_docs/metadata.json")
    if not metadata_path.exists():
        return {}

    with open(metadata_path, 'r') as f:
        return json.load(f)

def parse_datetime(dt_str: str) -> datetime:
    """Parse ISO datetime string"""
    return datetime.fromisoformat(dt_str)

def get_recent_updates(metadata: Dict, days: int = 7) -> Tuple[List[Dict], List[Dict]]:
    """Get recently updated and new documents"""
    cutoff_date = datetime.now() - timedelta(days=days)

    new_docs = []
    updated_docs = []

    for url, info in metadata.items():
        last_updated = parse_datetime(info['last_updated'])

        if last_updated > cutoff_date:
            doc_info = {
                'url': url,
                'filepath': info['filepath'],
                'last_updated': last_updated,
                'size': info['size_bytes']
            }

            # Check if it's truly new (updated = created within same minute)
            last_checked = parse_datetime(info['last_checked'])
            time_diff = abs((last_updated - last_checked).total_seconds())

            if time_diff < 60:  # Less than 1 minute difference = new file
                new_docs.append(doc_info)
            else:
                updated_docs.append(doc_info)

    # Sort by last_updated, most recent first
    new_docs.sort(key=lambda x: x['last_updated'], reverse=True)
    updated_docs.sort(key=lambda x: x['last_updated'], reverse=True)

    return new_docs, updated_docs

def categorize_by_section(metadata: Dict) -> Dict[str, int]:
    """Categorize files by documentation section"""
    categories = defaultdict(int)

    for info in metadata.values():
        filepath = info['filepath']

        if 'claude-code' in filepath:
            categories['Claude Code'] += 1
        elif 'build-with-claude' in filepath:
            categories['Build with Claude'] += 1
        elif 'about-claude' in filepath:
            categories['About Claude'] += 1
        elif 'agents-and-tools' in filepath:
            categories['Agents & Tools'] += 1
        elif 'test-and-evaluate' in filepath:
            categories['Test & Evaluate'] += 1
        elif 'release-notes' in filepath:
            categories['Release Notes'] += 1
        else:
            categories['Other'] += 1

    return dict(categories)

def generate_readme(metadata: Dict) -> str:
    """Generate README content"""

    # Get recent updates
    new_docs, updated_docs = get_recent_updates(metadata, days=7)

    # Calculate stats
    total_docs = len(metadata)
    total_size = sum(info['size_bytes'] for info in metadata.values()) / 1024 / 1024  # Convert to MB
    categories = categorize_by_section(metadata)

    # Get last update time
    if metadata:
        latest_update = max(parse_datetime(info['last_updated']) for info in metadata.values())
        last_update_str = latest_update.strftime('%Y-%m-%d %H:%M:%S UTC')
    else:
        last_update_str = "Never"

    # Get current timestamp for generation
    generated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")

    # Build README content
    readme = f"""# Anthropic Documentation Mirror

> Automatically updated mirror of [docs.claude.com](https://docs.claude.com) documentation

[![Daily Docs Update](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml/badge.svg)](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml)
![Total Docs](https://img.shields.io/badge/total_docs-{total_docs}-blue)
![Last Update](https://img.shields.io/badge/last_update-{latest_update.strftime('%Y--%m--%d')}-green)

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Total Documents** | {total_docs} |
| **Total Size** | {total_size:.2f} MB |
| **Last Updated** | {last_update_str} |
| **New This Week** | {len(new_docs)} |
| **Updated This Week** | {len(updated_docs)} |

---

## 📂 Documentation Categories

"""

    # Add category breakdown
    for category, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        percentage = (count / total_docs) * 100
        readme += f"- **{category}**: {count} documents ({percentage:.1f}%)\n"

    readme += "\n---\n\n"

    # Recent updates section
    if new_docs or updated_docs:
        readme += "## 🆕 Recent Updates (Last 7 Days)\n\n"

        if new_docs:
            readme += "### New Documents\n\n"
            for doc in new_docs[:10]:  # Show max 10
                date_str = doc['last_updated'].strftime('%Y-%m-%d')
                readme += f"- **[{doc['filepath']}]({doc['url']})** - {date_str}\n"

            if len(new_docs) > 10:
                readme += f"\n_...and {len(new_docs) - 10} more new documents_\n"

            readme += "\n"

        if updated_docs:
            readme += "### Updated Documents\n\n"
            for doc in updated_docs[:10]:  # Show max 10
                date_str = doc['last_updated'].strftime('%Y-%m-%d')
                readme += f"- **[{doc['filepath']}]({doc['url']})** - {date_str}\n"

            if len(updated_docs) > 10:
                readme += f"\n_...and {len(updated_docs) - 10} more updated documents_\n"

        readme += "\n---\n\n"

    # About section
    readme += f"""## 📖 About

This repository contains an automated mirror of Anthropic's official documentation from [docs.claude.com](https://docs.claude.com).

### Features

- 🤖 **Automated Updates** - Runs daily at 6:00 AM MST/MDT
- 📝 **Direct Markdown** - Downloads pre-generated `.md` files for better quality
- 🔍 **Change Detection** - MD5 hashing tracks updates efficiently
- 📊 **Statistics** - Automatic README updates with latest stats
- 🔄 **Full Mirror** - Maintains complete directory structure

### How It Works

1. GitHub Actions workflow runs daily
2. Scraper fetches all documentation pages
3. Downloads pre-generated markdown files (with HTML fallback)
4. Detects changes via MD5 hash comparison
5. Commits updates and regenerates this README

---

## 🗂️ Repository Structure

```
claude_docs_scraper/
├── anthropic_docs/           # Downloaded documentation
│   ├── docs/                 # Main documentation
│   ├── release-notes/        # Release notes
│   └── metadata.json         # Change tracking
├── scraper.py                # Main scraper script
├── generate_readme_stats.py  # README generator
└── .github/workflows/        # Automation workflows
```

---

## 🚀 Usage

### Browse Documentation

Navigate through `anthropic_docs/docs/` to read the documentation in markdown format.

### Run Scraper Locally

```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run once
python3 scraper.py --once

# Continuous monitoring (checks every 60 minutes)
python3 scraper.py
```

### Generate Stats

```bash
python3 generate_readme_stats.py
```

---

## 📅 Update Schedule

- **Automated**: Daily at 6:00 AM MST/MDT
- **Manual**: Can be triggered via [Actions tab](https://github.com/seanGSISG/claude_docs_scraper/actions)

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details

Documentation content © Anthropic - [docs.claude.com](https://docs.claude.com)

---

## 🔗 Links

- **Official Docs**: [docs.claude.com](https://docs.claude.com)
- **Anthropic**: [anthropic.com](https://www.anthropic.com)
- **Claude**: [claude.ai](https://claude.ai)

---

**Last Generated**: {generated_time}
"""

    return readme

def main():
    """Main entry point"""
    print("Loading metadata...")
    metadata = load_metadata()

    if not metadata:
        print("No metadata found. Run scraper first.")
        return

    print(f"Generating README for {len(metadata)} documents...")
    readme_content = generate_readme(metadata)

    print("Writing README.md...")
    with open("README.md", 'w') as f:
        f.write(readme_content)

    print("✓ README.md generated successfully!")

if __name__ == "__main__":
    main()
