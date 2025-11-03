Source: https://docs.claude.com/en/docs/build-with-claude/define-success
Last fetched: 2025-11-03T13:14:02.779164
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
Test & evaluate
Define your success criteria
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
Building strong criteria
Common success criteria to consider
Next steps
Building a successful LLM-based application starts with clearly defining your success criteria. How will you know when your application is good enough to publish?
Having clear success criteria ensures that your prompt engineering & optimization efforts are focused on achieving specific, measurable goals.
​
Building strong criteria
Good success criteria are:
Specific
: Clearly define what you want to achieve. Instead of “good performance,” specify “accurate sentiment classification.”
Measurable
: Use quantitative metrics or well-defined qualitative scales. Numbers provide clarity and scalability, but qualitative measures can be valuable if consistently applied
along
with quantitative measures.
Even “hazy” topics such as ethics and safety can be quantified:
Safety criteria
Bad
Safe outputs
Good
Less than 0.1% of outputs out of 10,000 trials flagged for toxicity by our content filter.
Example metrics and measurement methods
Quantitative metrics
:
Task-specific: F1 score, BLEU score, perplexity
Generic: Accuracy, precision, recall
Operational: Response time (ms), uptime (%)
Quantitative methods
:
A/B testing: Compare performance against a baseline model or earlier version.
User feedback: Implicit measures like task completion rates.
Edge case analysis: Percentage of edge cases handled without errors.
Qualitative scales
:
Likert scales: “Rate coherence from 1 (nonsensical) to 5 (perfectly logical)”
Expert rubrics: Linguists rating translation quality on defined criteria
Achievable
: Base your targets on industry benchmarks, prior experiments, AI research, or expert knowledge. Your success metrics should not be unrealistic to current frontier model capabilities.
Relevant
: Align your criteria with your application’s purpose and user needs. Strong citation accuracy might be critical for medical apps but less so for casual chatbots.
Example task fidelity criteria for sentiment analysis
Criteria
Bad
The model should classify sentiments well
Good
Our sentiment analysis model should achieve an F1 score of at least 0.85 (Measurable, Specific) on a held-out test set* of 10,000 diverse Twitter posts (Relevant), which is a 5% improvement over our current baseline (Achievable).
*
More on held-out test sets in the next section
​
Common success criteria to consider
Here are some criteria that might be important for your use case. This list is non-exhaustive.
Task fidelity
How well does the model need to perform on the task? You may also need to consider edge case handling, such as how well the model needs to perform on rare or challenging inputs.
Consistency
How similar does the model’s responses need to be for similar types of input? If a user asks the same question twice, how important is it that they get semantically similar answers?
Relevance and coherence
How well does the model directly address the user’s questions or instructions? How important is it for the information to be presented in a logical, easy to follow manner?
Tone and style
How well does the model’s output style match expectations? How appropriate is its language for the target audience?
Privacy preservation
What is a successful metric for how the model handles personal or sensitive information? Can it follow instructions not to use or share certain details?
Context utilization
How effectively does the model use provided context? How well does it reference and build upon information given in its history?
Latency
What is the acceptable response time for the model? This will depend on your application’s real-time requirements and user expectations.
Price
What is your budget for running the model? Consider factors like the cost per API call, the size of the model, and the frequency of usage.
Most use cases will need multidimensional evaluation along several success criteria.
Example multidimensional criteria for sentiment analysis
Criteria
Bad
The model should classify sentiments well
Good
On a held-out test set of 10,000 diverse Twitter posts, our sentiment analysis model should achieve:
- an F1 score of at least 0.85
- 99.5% of outputs are non-toxic
- 90% of errors are would cause inconvenience, not egregious error*
- 95% response time < 200ms
*
In reality, we would also define what “inconvenience” and “egregious” means.
​
Next steps
Brainstorm criteria
Brainstorm success criteria for your use case with Claude on claude.ai.
Tip
: Drop this page into the chat as guidance for Claude!
Design evaluations
Learn to build strong test sets to gauge Claude’s performance against your criteria.
Was this page helpful?
Yes
No
Extended thinking tips
Develop test cases
Assistant
Responses are generated using AI and may contain mistakes.