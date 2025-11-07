# Anthropic Documentation Mirror

> Automatically updated mirror of [docs.claude.com](https://docs.claude.com) documentation

[![Daily Docs Update](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml/badge.svg)](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml)
![Total Docs](https://img.shields.io/badge/total_docs-187-blue)
![Last Update](https://img.shields.io/badge/last_update-2025--11--07-green)

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Total Documents** | 187 |
| **Total Size** | 2.51 MB |
| **Last Updated** | 2025-11-07 12:05:42 UTC |
| **New This Week** | 186 |
| **Updated This Week** | 0 |

---

## 📂 Documentation Categories

- **Claude Code**: 60 documents (32.1%)
- **Other**: 37 documents (19.8%)
- **Build with Claude**: 37 documents (19.8%)
- **Agents & Tools**: 23 documents (12.3%)
- **About Claude**: 16 documents (8.6%)
- **Test & Evaluate**: 11 documents (5.9%)
- **Release Notes**: 3 documents (1.6%)

---

## 🆕 Recent Updates (Last 7 Days)

### New Documents

- **[docs/en/claude-code-on-the-web.md](https://docs.claude.com/docs/en/claude-code-on-the-web)** - 2025-11-07
- **[docs/build-with-claude/pdf-support.md](https://docs.claude.com/en/docs/build-with-claude/pdf-support)** - 2025-11-07
- **[docs/build-with-claude/prompt-engineering.md](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering)** - 2025-11-07
- **[docs/claude-code/overview.md](https://docs.claude.com/en/docs/claude-code/overview)** - 2025-11-07
- **[docs/build-with-claude/prompt-engineering/long-context-tips.md](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/long-context-tips)** - 2025-11-07
- **[docs/agents-and-tools/agent-skills/quickstart.md](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/quickstart)** - 2025-11-07
- **[docs/agents-and-tools/tool-use/bash-tool.md](https://docs.claude.com/en/docs/agents-and-tools/tool-use/bash-tool)** - 2025-11-07
- **[docs/mcp.md](https://docs.claude.com/en/docs/mcp)** - 2025-11-07
- **[docs/about-claude/use-case-guides.md](https://docs.claude.com/en/docs/about-claude/use-case-guides)** - 2025-11-07
- **[docs/prompt-generator.md](https://docs.claude.com/en/docs/prompt-generator)** - 2025-11-07

_...and 176 more new documents_


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

**Last Generated**: 2025-11-07 12:05:43 UTC
