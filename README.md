# Anthropic Documentation Mirror

> Automatically updated mirror of [docs.claude.com](https://docs.claude.com) documentation

[![Daily Docs Update](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml/badge.svg)](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml)
![Total Docs](https://img.shields.io/badge/total_docs-144-blue)
![Last Update](https://img.shields.io/badge/last_update-2025--11--01-green)

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Total Documents** | 144 |
| **Total Size** | 2.48 MB |
| **Last Updated** | 2025-11-01 13:10:37 UTC |
| **New This Week** | 143 |
| **Updated This Week** | 0 |

---

## 📂 Documentation Categories

- **Claude Code**: 50 documents (34.7%)
- **Build with Claude**: 37 documents (25.7%)
- **Agents & Tools**: 20 documents (13.9%)
- **About Claude**: 16 documents (11.1%)
- **Test & Evaluate**: 11 documents (7.6%)
- **Other**: 7 documents (4.9%)
- **Release Notes**: 3 documents (2.1%)

---

## 🆕 Recent Updates (Last 7 Days)

### New Documents

- **[docs/about-claude/use-case-guides.md](https://docs.claude.com/en/docs/about-claude/use-case-guides)** - 2025-11-01
- **[docs/build-with-claude/text-generation.md](https://docs.claude.com/en/docs/build-with-claude/text-generation)** - 2025-11-01
- **[docs/build-with-claude/prompt-engineering/extended-thinking-tips.md](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/extended-thinking-tips)** - 2025-11-01
- **[docs/claude-code/memory.md](https://docs.claude.com/en/docs/claude-code/memory)** - 2025-11-01
- **[docs/build-with-claude/prompt-engineering/chain-prompts.md](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-prompts)** - 2025-11-01
- **[docs/claude-code/amazon-bedrock.md](https://docs.claude.com/en/docs/claude-code/amazon-bedrock)** - 2025-11-01
- **[docs/claude-code/github-actions.md](https://docs.claude.com/en/docs/claude-code/github-actions)** - 2025-11-01
- **[docs/agents-and-tools/tool-use/overview.md](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)** - 2025-11-01
- **[docs/claude-code/terminal-config.md](https://docs.claude.com/en/docs/claude-code/terminal-config)** - 2025-11-01
- **[docs/claude-code/data-usage.md](https://docs.claude.com/en/docs/claude-code/data-usage)** - 2025-11-01

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

**Last Generated**: 2025-11-01 13:10:38 UTC
