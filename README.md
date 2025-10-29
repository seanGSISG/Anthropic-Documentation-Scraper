# Anthropic Documentation Mirror

> Automatically updated mirror of [docs.claude.com](https://docs.claude.com) documentation

[![Daily Docs Update](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml/badge.svg)](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml)
![Total Docs](https://img.shields.io/badge/total_docs-143-blue)
![Last Update](https://img.shields.io/badge/last_update-2025--10--29-green)

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Total Documents** | 143 |
| **Total Size** | 2.45 MB |
| **Last Updated** | 2025-10-29 13:16:45 UTC |
| **New This Week** | 143 |
| **Updated This Week** | 0 |

---

## 📂 Documentation Categories

- **Claude Code**: 50 documents (35.0%)
- **Build with Claude**: 36 documents (25.2%)
- **Agents & Tools**: 20 documents (14.0%)
- **About Claude**: 16 documents (11.2%)
- **Test & Evaluate**: 11 documents (7.7%)
- **Other**: 7 documents (4.9%)
- **Release Notes**: 3 documents (2.1%)

---

## 🆕 Recent Updates (Last 7 Days)

### New Documents

- **[docs/build-with-claude/develop-tests.md](https://docs.claude.com/en/docs/build-with-claude/develop-tests)** - 2025-10-29
- **[docs/claude-code/common-workflows.md](https://docs.claude.com/en/docs/claude-code/common-workflows)** - 2025-10-29
- **[docs/about-claude/glossary.md](https://docs.claude.com/en/docs/about-claude/glossary)** - 2025-10-29
- **[docs/about-claude/use-case-guides/content-moderation.md](https://docs.claude.com/en/docs/about-claude/use-case-guides/content-moderation)** - 2025-10-29
- **[docs/build-with-claude/computer-use.md](https://docs.claude.com/en/docs/build-with-claude/computer-use)** - 2025-10-29
- **[docs/about-claude/models/choosing-a-model.md](https://docs.claude.com/en/docs/about-claude/models/choosing-a-model)** - 2025-10-29
- **[docs/claude-code/plugins.md](https://docs.claude.com/en/docs/claude-code/plugins)** - 2025-10-29
- **[docs/claude-code/hooks.md](https://docs.claude.com/en/docs/claude-code/hooks)** - 2025-10-29
- **[docs/claude-code/llm-gateway.md](https://docs.claude.com/en/docs/claude-code/llm-gateway)** - 2025-10-29
- **[docs/about-claude/models/extended-thinking-models.md](https://docs.claude.com/en/docs/about-claude/models/extended-thinking-models)** - 2025-10-29

_...and 133 more new documents_


---

## 📖 About

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

**Last Generated**: 2025-10-29 13:16:45 UTC
