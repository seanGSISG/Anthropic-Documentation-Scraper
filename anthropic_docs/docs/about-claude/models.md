Source: https://docs.claude.com/en/docs/about-claude/models
Last fetched: 2025-11-13T13:15:57.198593
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
Models & pricing
Models overview
Home
Developer Guide
API Reference
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
Using the Messages API
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
Using Skills with the API
Agent SDK
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
Choosing a model
Latest models comparison
Prompt and output performance
Migrating to Claude 4.5
Get started with Claude
​
Choosing a model
If you’re unsure which model to use, we recommend starting with
Claude Sonnet 4.5
. It offers the best balance of intelligence, speed, and cost for most use cases, with exceptional performance in coding and agentic tasks.
All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Anthropic API, AWS Bedrock, and Google Vertex AI.
Once you’ve picked a model,
learn how to make your first API call
.
​
Latest models comparison
Feature
Claude Sonnet 4.5
Claude Haiku 4.5
Claude Opus 4.1
Description
Our smartest model for complex agents and coding
Our fastest model with near-frontier intelligence
Exceptional model for specialized reasoning tasks
Claude API ID
claude-sonnet-4-5-20250929
Copied!
claude-haiku-4-5-20251001
Copied!
claude-opus-4-1-20250805
Copied!
Claude API alias
1
claude-sonnet-4-5
Copied!
claude-haiku-4-5
Copied!
claude-opus-4-1
Copied!
AWS Bedrock ID
anthropic.claude-sonnet-4-5-20250929-v1:0
Copied!
anthropic.claude-haiku-4-5-20251001-v1:0
Copied!
anthropic.claude-opus-4-1-20250805-v1:0
Copied!
GCP Vertex AI ID
claude-sonnet-4-5@20250929
Copied!
claude-haiku-4-5@20251001
Copied!
claude-opus-4-1@20250805
Copied!
Pricing
2
$3 / input MTok
$15 / output MTok
$1 / input MTok
$5 / output MTok
$15 / input MTok
$75 / output MTok
Extended thinking
Yes
Yes
Yes
Priority Tier
Yes
Yes
Yes
Comparative latency
Fast
Fastest
Moderate
Context window
200K tokens
/
1M tokens
(beta)
3
200K tokens
200K tokens
Max output
64K tokens
64K tokens
32K tokens
Reliable knowledge cutoff
Jan 2025
4
Feb 2025
Jan 2025
4
Training data cutoff
Jul 2025
Jul 2025
Mar 2025
1 - Aliases automatically point to the most recent model snapshot. When we release new model snapshots, we migrate aliases to point to the newest version of a model, typically within a week of the new release. While aliases are useful for experimentation, we recommend using specific model versions (e.g.,
claude-sonnet-4-5-20250929
) in production applications to ensure consistent behavior.
2 - See our
pricing page
for complete pricing information including batch API discounts, prompt caching rates, extended thinking costs, and vision processing fees.
3 - Claude Sonnet 4.5 supports a
1M token context window
when using the
context-1m-2025-08-07
beta header.
Long context pricing
applies to requests exceeding 200K tokens.
4 -
Reliable knowledge cutoff
indicates the date through which a model’s knowledge is most extensive and reliable.
Training data cutoff
is the broader date range of training data used. For example, Claude Sonnet 4.5 was trained on publicly available information through July 2025, but its knowledge is most extensive and reliable through January 2025. For more information, see
Anthropic’s Transparency Hub
.
Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.
Starting with
Claude Sonnet 4.5 and all future models
, AWS Bedrock and Google Vertex AI offer two endpoint types:
global endpoints
(dynamic routing for maximum availability) and
regional endpoints
(guaranteed data routing through specific geographic regions). For more information, see the
third-party platform pricing section
.
Legacy models
The following models are still available but we recommend migrating to current models for improved performance:
Feature
Claude Sonnet 4
Claude Sonnet 3.7
Claude Opus 4
Claude Haiku 3.5
Claude Haiku 3
Claude API ID
claude-sonnet-4-20250514
Copied!
claude-3-7-sonnet-20250219
Copied!
claude-opus-4-20250514
Copied!
claude-3-5-haiku-20241022
Copied!
claude-3-haiku-20240307
Copied!
Claude API alias
claude-sonnet-4-0
Copied!
claude-3-7-sonnet-latest
Copied!
claude-opus-4-0
Copied!
claude-3-5-haiku-latest
Copied!
—
AWS Bedrock ID
anthropic.claude-sonnet-4-20250514-v1:0
Copied!
anthropic.claude-3-7-sonnet-20250219-v1:0
Copied!
anthropic.claude-opus-4-20250514-v1:0
Copied!
anthropic.claude-3-5-haiku-20241022-v1:0
Copied!
anthropic.claude-3-haiku-20240307-v1:0
Copied!
GCP Vertex AI ID
claude-sonnet-4@20250514
Copied!
claude-3-7-sonnet@20250219
Copied!
claude-opus-4@20250514
Copied!
claude-3-5-haiku@20241022
Copied!
claude-3-haiku@20240307
Copied!
Pricing
$3 / input MTok
$15 / output MTok
$3 / input MTok
$15 / output MTok
$15 / input MTok
$75 / output MTok
$0.80 / input MTok
$4 / output MTok
$0.25 / input MTok
$1.25 / output MTok
Extended thinking
Yes
Yes
Yes
No
No
Priority Tier
Yes
Yes
Yes
Yes
No
Comparative latency
Fast
Fast
Moderate
Fastest
Fast
Context window
200K tokens
/
1M tokens
(beta)
1
200K tokens
200K tokens
200K tokens
200K tokens
Max output
64K tokens
64K tokens / 128K tokens (beta)
4
32K tokens
8K tokens
4K tokens
Reliable knowledge cutoff
Jan 2025
2
Oct 2024
2
Jan 2025
2
3
3
Training data cutoff
Mar 2025
Nov 2024
Mar 2025
Jul 2024
Aug 2023
1 - Claude Sonnet 4 supports a
1M token context window
when using the
context-1m-2025-08-07
beta header.
Long context pricing
applies to requests exceeding 200K tokens.
2 -
Reliable knowledge cutoff
indicates the date through which a model’s knowledge is most extensive and reliable.
Training data cutoff
is the broader date range of training data used.
3 - Some Haiku models have a single training data cutoff date.
4 - Include the beta header
output-128k-2025-02-19
in your API request to increase the maximum output token length to 128K tokens for Claude Sonnet 3.7. We strongly suggest using our
streaming Messages API
to avoid timeouts when generating longer outputs. See our guidance on
long requests
for more details.
​
Prompt and output performance
Claude 4 models excel in:
Performance
: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the
Claude 4 blog post
for more information.
Engaging responses
: Claude models are ideal for applications that require rich, human-like interactions.
If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our
prompt engineering guides
for details.
For specific Claude 4 prompting best practices, see our
Claude 4 best practices guide
.
Output quality
: When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.
​
Migrating to Claude 4.5
If you’re currently using Claude 3 models, we recommend migrating to Claude 4.5 to take advantage of improved intelligence and enhanced capabilities. For detailed migration instructions, see
Migrating to Claude 4.5
.
​
Get started with Claude
If you’re ready to start exploring what Claude can do for you, let’s dive in! Whether you’re a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we’ve got you covered.
Looking to chat with Claude? Visit
claude.ai
!
Intro to Claude
Explore Claude’s capabilities and development flow.
Quickstart
Learn how to make your first API call in minutes.
Claude Console
Craft and test powerful prompts directly in your browser.
If you have any questions or need assistance, don’t hesitate to reach out to our
support team
or consult the
Discord community
.
Was this page helpful?
Yes
No
Quickstart
Choosing a model
Assistant
Responses are generated using AI and may contain mistakes.