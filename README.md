# Anthropic Documentation Mirror

> Automatically updated mirror of [docs.claude.com](https://docs.claude.com) documentation

[![Daily Docs Update](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml/badge.svg)](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml)
![Total Docs](https://img.shields.io/badge/total_docs-212-blue)
![Last Update](https://img.shields.io/badge/last_update-2025--11--19-green)

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Total Documents** | 212 |
| **Total Size** | 2.94 MB |
| **Last Updated** | 2025-11-19 12:05:57 UTC |
| **New This Week** | 133 |
| **Updated This Week** | 0 |

---

## 📂 Documentation Categories

- **Claude Code**: 61 documents (28.8%)
- **Other**: 54 documents (25.5%)
- **Build with Claude**: 44 documents (20.8%)
- **Agents & Tools**: 23 documents (10.8%)
- **About Claude**: 16 documents (7.5%)
- **Test & Evaluate**: 11 documents (5.2%)
- **Release Notes**: 3 documents (1.4%)

---

## 🆕 Recent Updates (Last 7 Days)

### New Documents

- **[docs/agent-sdk/overview.md](https://docs.claude.com/en/docs/agent-sdk/overview)** - 2025-11-19
- **[docs/agents-and-tools/agent-skills/overview.md](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)** - 2025-11-19
- **[docs/build-with-claude/overview.md](https://docs.claude.com/en/docs/build-with-claude/overview)** - 2025-11-19
- **[docs/about-claude/use-case-guides.md](https://docs.claude.com/en/docs/about-claude/use-case-guides)** - 2025-11-19
- **[docs/agent-sdk/sessions.md](https://docs.claude.com/en/docs/agent-sdk/sessions)** - 2025-11-19
- **[docs/agent-sdk/modifying-system-prompts.md](https://docs.claude.com/en/docs/agent-sdk/modifying-system-prompts)** - 2025-11-19
- **[docs/about-claude/glossary.md](https://docs.claude.com/en/docs/about-claude/glossary)** - 2025-11-19
- **[docs/build-with-claude/extended-thinking.md](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)** - 2025-11-19
- **[docs/about-claude/models.md](https://docs.claude.com/en/docs/about-claude/models)** - 2025-11-19
- **[docs/agent-sdk/streaming-vs-single-mode.md](https://docs.claude.com/en/docs/agent-sdk/streaming-vs-single-mode)** - 2025-11-19

_...and 123 more new documents_


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

**Last Generated**: 2025-11-19 12:05:58 UTC
