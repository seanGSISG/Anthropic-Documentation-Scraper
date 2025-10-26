Source: https://docs.claude.com/en/docs/build-with-claude/prompt-engineering
Last fetched: 2025-10-26T13:10:47.055058
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
Prompt engineering overview
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
Features overview
Models & pricing
Models overview
Choosing a model
What's new in Claude 4.5
Migrating to Claude 4.5
Model deprecations
Pricing
Capabilities
Context windows
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
Claude 4 best practices
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
On this page
Before prompt engineering
When to prompt engineer
How to prompt engineer
Prompt engineering tutorial
While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models
here
.
​
Before prompt engineering
This guide assumes that you have:
A clear definition of the success criteria for your use case
Some ways to empirically test against those criteria
A first draft prompt you want to improve
If not, we highly suggest you spend time establishing that first. Check out
Define your success criteria
and
Create strong empirical evaluations
for tips and guidance.
Prompt generator
Don’t have a first draft prompt? Try the prompt generator in the Claude Console!
​
When to prompt engineer
This guide focuses on success criteria that are controllable through prompt engineering.
Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.
Prompting vs. finetuning
Prompt engineering is far faster than other methods of model behavior control, such as finetuning, and can often yield leaps in performance in far less time. Here are some reasons to consider prompt engineering over finetuning:
Resource efficiency
: Fine-tuning requires high-end GPUs and large memory, while prompt engineering only needs text input, making it much more resource-friendly.
Cost-effectiveness
: For cloud-based AI services, fine-tuning incurs significant costs. Prompt engineering uses the base model, which is typically cheaper.
Maintaining model updates
: When providers update models, fine-tuned versions might need retraining. Prompts usually work across versions without changes.
Time-saving
: Fine-tuning can take hours or even days. In contrast, prompt engineering provides nearly instantaneous results, allowing for quick problem-solving.
Minimal data needs
: Fine-tuning needs substantial task-specific, labeled data, which can be scarce or expensive. Prompt engineering works with few-shot or even zero-shot learning.
Flexibility & rapid iteration
: Quickly try various approaches, tweak prompts, and see immediate results. This rapid experimentation is difficult with fine-tuning.
Domain adaptation
: Easily adapt models to new domains by providing domain-specific context in prompts, without retraining.
Comprehension improvements
: Prompt engineering is far more effective than finetuning at helping models better understand and utilize external content such as retrieved documents
Preserves general knowledge
: Fine-tuning risks catastrophic forgetting, where the model loses general knowledge. Prompt engineering maintains the model’s broad capabilities.
Transparency
: Prompts are human-readable, showing exactly what information the model receives. This transparency aids in understanding and debugging.
​
How to prompt engineer
The prompt engineering pages in this section have been organized from most broadly effective techniques to more specialized techniques. When troubleshooting performance, we suggest you try these techniques in order, although the actual impact of each technique will depend on your use case.
Prompt generator
Be clear and direct
Use examples (multishot)
Let Claude think (chain of thought)
Use XML tags
Give Claude a role (system prompts)
Prefill Claude’s response
Chain complex prompts
Long context tips
​
Prompt engineering tutorial
If you’re an interactive learner, you can dive into our interactive tutorials instead!
GitHub prompting tutorial
An example-filled tutorial that covers the prompt engineering concepts found in our docs.
Google Sheets prompting tutorial
A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.
Was this page helpful?
Yes
No
Vertex AI
Claude 4 best practices
Assistant
Responses are generated using AI and may contain mistakes.