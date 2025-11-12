# Anthropic Documentation Mirror

> Automatically updated mirror of [docs.claude.com](https://docs.claude.com) documentation

[![Daily Docs Update](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml/badge.svg)](https://github.com/seanGSISG/claude_docs_scraper/actions/workflows/daily-scraper.yml)
![Total Docs](https://img.shields.io/badge/total_docs-209-blue)
![Last Update](https://img.shields.io/badge/last_update-2025--11--12-green)

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| **Total Documents** | 209 |
| **Total Size** | 2.87 MB |
| **Last Updated** | 2025-11-12 12:05:46 UTC |
| **New This Week** | 208 |
| **Updated This Week** | 0 |

---

## 📂 Documentation Categories

- **Claude Code**: 61 documents (29.2%)
- **Other**: 53 documents (25.4%)
- **Build with Claude**: 42 documents (20.1%)
- **Agents & Tools**: 23 documents (11.0%)
- **About Claude**: 16 documents (7.7%)
- **Test & Evaluate**: 11 documents (5.3%)
- **Release Notes**: 3 documents (1.4%)

---

## 🆕 Recent Updates (Last 7 Days)

### New Documents

- **[docs/agent-sdk/streaming-vs-single-mode.md](https://docs.claude.com/en/docs/agent-sdk/streaming-vs-single-mode)** - 2025-11-12
- **[docs/en/data-usage.md](https://docs.claude.com/docs/en/data-usage)** - 2025-11-12
- **[docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md](https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)** - 2025-11-12
- **[docs/test-and-evaluate/strengthen-guardrails/increase-consistency.md](https://docs.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/increase-consistency)** - 2025-11-12
- **[docs/en/vs-code.md](https://docs.claude.com/docs/en/vs-code)** - 2025-11-12
- **[docs/about-claude/glossary.md](https://docs.claude.com/en/docs/about-claude/glossary)** - 2025-11-12
- **[docs/en/cli-reference.md](https://docs.claude.com/docs/en/cli-reference)** - 2025-11-12
- **[docs/intro.md](https://docs.claude.com/en/docs/intro)** - 2025-11-12
- **[docs/agents-and-tools/agent-skills/overview.md](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)** - 2025-11-12
- **[docs/en/common-workflows.md](https://docs.claude.com/docs/en/common-workflows)** - 2025-11-12

_...and 198 more new documents_


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

**Last Generated**: 2025-11-12 12:05:46 UTC
