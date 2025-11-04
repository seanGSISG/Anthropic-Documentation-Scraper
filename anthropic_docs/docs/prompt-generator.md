Source: https://docs.claude.com/en/docs/prompt-generator
Last fetched: 2025-11-04T12:05:04.459588
Note: Extracted from HTML (no .md endpoint available)

---

Agent Skills are now available!
Learn more about extending Claude's capabilities with Agent Skills
.
Claude Docs
home page
English
Search...
⌘
K
Search...
Navigation
Prompt engineering
Automatically generate first draft prompt templates
Home
Developer Guide
API Reference
Claude Code
Model Context Protocol (MCP)
Resources
Release Notes
First steps
Intro to Claude
Quickstart
Models & pricing
Models overview
Choosing a model
What's new in Claude 4.5
Migrating to Claude 4.5
Model deprecations
Pricing
Build with Claude
Features overview
Working with the Messages API
Context windows
Prompting best practices
Capabilities
Prompt caching
Context editing
Extended thinking
Streaming Messages
Batch processing
Citations
Multilingual support
Token counting
Embeddings
Vision
PDF support
Files API
Search results
Google Sheets add-on
Tools
Overview
How to implement tool use
Token-efficient tool use
Fine-grained tool streaming
Bash tool
Code execution tool
Computer use tool
Text editor tool
Web fetch tool
Web search tool
Memory tool
Agent Skills
Overview
Quickstart
Best practices
Using Skills
Agent SDK
Migrate to Claude Agent SDK
Overview
TypeScript SDK
Python SDK
Guides
MCP in the API
MCP connector
Remote MCP servers
Claude on 3rd-party platforms
Amazon Bedrock
Vertex AI
Prompt engineering
Overview
Prompt generator
Use prompt templates
Prompt improver
Be clear and direct
Use examples (multishot prompting)
Let Claude think (CoT)
Use XML tags
Give Claude a role (system prompts)
Prefill Claude's response
Chain complex prompts
Long context tips
Extended thinking tips
Test & evaluate
Define success criteria
Develop test cases
Using the Evaluation Tool
Reducing latency
Strengthen guardrails
Reduce hallucinations
Increase output consistency
Mitigate jailbreaks
Streaming refusals
Reduce prompt leak
Keep Claude in character
Administration and monitoring
Admin API overview
Usage and Cost API
Claude Code Analytics API
On this page
Next steps
Our prompt generator is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see
here
.
Sometimes, the hardest part of using an AI model is figuring out how to prompt it effectively. To help with this, we’ve created a prompt generation tool that guides Claude to generate high-quality prompt templates tailored to your specific tasks. These templates follow many of our prompt engineering best practices.
The prompt generator is particularly useful as a tool for solving the “blank page problem” to give you a jumping-off point for further testing and iteration.
Try the prompt generator now directly on the
Console
.
If you’re interested in analyzing the underlying prompt and architecture, check out our
prompt generator Google Colab notebook
. There, you can easily run the code to have Claude construct prompts on your behalf.
Note that to run the Colab notebook, you will need an
API key
.
​
Next steps
Start prompt engineering
Get inspired by a curated selection of prompts for various tasks and use cases.
Prompt library
Get inspired by a curated selection of prompts for various tasks and use cases.
GitHub prompting tutorial
An example-filled tutorial that covers the prompt engineering concepts found in our docs.
Google Sheets prompting tutorial
A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
Was this page helpful?
Yes
No
Overview
Use prompt templates
Assistant
Responses are generated using AI and may contain mistakes.