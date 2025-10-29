Source: https://docs.claude.com/en/docs/claude-code/sdk
Last fetched: 2025-10-29T12:05:24.084567
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
Agent SDK
Migrate to Claude Agent SDK
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
On this page
Overview
What’s Changed
Migration Steps
For TypeScript/JavaScript Projects
For Python Projects
Breaking changes
Python: ClaudeCodeOptions renamed to ClaudeAgentOptions
System prompt no longer default
Settings Sources No Longer Loaded by Default
Why the Rename?
Getting Help
Next Steps
​
Overview
The Claude Code SDK has been renamed to the
Claude Agent SDK
and its documentation has been reorganized. This change reflects the SDK’s broader capabilities for building AI agents beyond just coding tasks.
​
What’s Changed
Aspect
Old
New
Package Name (TS/JS)
@anthropic-ai/claude-code
@anthropic-ai/claude-agent-sdk
Python Package
claude-code-sdk
claude-agent-sdk
Documentation Location
Claude Code docs → SDK section
API Guide → Agent SDK section
Documentation Changes:
The Agent SDK documentation has moved from the Claude Code docs to the API Guide under a dedicated
Agent SDK
section. The Claude Code docs now focus on the CLI tool and automation features.
​
Migration Steps
​
For TypeScript/JavaScript Projects
1. Uninstall the old package:
Copy
npm
uninstall
@anthropic-ai/claude-code
2. Install the new package:
Copy
npm
install
@anthropic-ai/claude-agent-sdk
3. Update your imports:
Change all imports from
@anthropic-ai/claude-code
to
@anthropic-ai/claude-agent-sdk
:
Copy
// Before
import
{
query
,
tool
,
createSdkMcpServer
}
from
"@anthropic-ai/claude-code"
;
// After
import
{
query
,
tool
,
createSdkMcpServer
,
}
from
"@anthropic-ai/claude-agent-sdk"
;
4. Update package.json dependencies:
If you have the package listed in your
package.json
, update it:
Copy
// Before
{
"dependencies"
: {
"@anthropic-ai/claude-code"
:
"^1.0.0"
}
}
// After
{
"dependencies"
: {
"@anthropic-ai/claude-agent-sdk"
:
"^0.1.0"
}
}
That’s it! No other code changes are required.
​
For Python Projects
1. Uninstall the old package:
Copy
pip
uninstall
claude-code-sdk
2. Install the new package:
Copy
pip
install
claude-agent-sdk
3. Update your imports:
Change all imports from
claude_code_sdk
to
claude_agent_sdk
:
Copy
# Before
from
claude_code_sdk
import
query, ClaudeCodeOptions
# After
from
claude_agent_sdk
import
query, ClaudeAgentOptions
4. Update type names:
Change
ClaudeCodeOptions
to
ClaudeAgentOptions
:
Copy
# Before
from
claude_agent_sdk
import
query, ClaudeCodeOptions
options
=
ClaudeCodeOptions(
model
=
"claude-sonnet-4-5"
)
# After
from
claude_agent_sdk
import
query, ClaudeAgentOptions
options
=
ClaudeAgentOptions(
model
=
"claude-sonnet-4-5"
)
5. Review
breaking changes
Make any code changes needed to complete the migration.
​
Breaking changes
To improve isolation and explicit configuration, Claude Agent SDK v0.1.0 introduces breaking changes for users migrating from Claude Code SDK. Review this section carefully before migrating.
​
Python: ClaudeCodeOptions renamed to ClaudeAgentOptions
What changed:
The Python SDK type
ClaudeCodeOptions
has been renamed to
ClaudeAgentOptions
.
Migration:
Copy
# BEFORE (v0.0.x)
from
claude_agent_sdk
import
query, ClaudeCodeOptions
options
=
ClaudeCodeOptions(
model
=
"claude-sonnet-4-5"
,
permission_mode
=
"acceptEdits"
)
# AFTER (v0.1.0)
from
claude_agent_sdk
import
query, ClaudeAgentOptions
options
=
ClaudeAgentOptions(
model
=
"claude-sonnet-4-5"
,
permission_mode
=
"acceptEdits"
)
Why this changed:
The type name now matches the “Claude Agent SDK” branding and provides consistency across the SDK’s naming conventions.
​
System prompt no longer default
What changed:
The SDK no longer uses Claude Code’s system prompt by default.
Migration:
TypeScript
Python
Copy
// BEFORE (v0.0.x) - Used Claude Code's system prompt by default
const
result
=
query
({
prompt:
"Hello"
});
// AFTER (v0.1.0) - Uses empty system prompt by default
// To get the old behavior, explicitly request Claude Code's preset:
const
result
=
query
({
prompt:
"Hello"
,
options:
{
systemPrompt:
{
type:
"preset"
,
preset:
"claude_code"
}
}
});
// Or use a custom system prompt:
const
result
=
query
({
prompt:
"Hello"
,
options:
{
systemPrompt:
"You are a helpful coding assistant"
}
});
Why this changed:
Provides better control and isolation for SDK applications. You can now build agents with custom behavior without inheriting Claude Code’s CLI-focused instructions.
​
Settings Sources No Longer Loaded by Default
What changed:
The SDK no longer reads from filesystem settings (CLAUDE.md, settings.json, slash commands, etc.) by default.
Migration:
TypeScript
Python
Copy
// BEFORE (v0.0.x) - Loaded all settings automatically
const
result
=
query
({
prompt:
"Hello"
});
// Would read from:
// - ~/.claude/settings.json (user)
// - .claude/settings.json (project)
// - .claude/settings.local.json (local)
// - CLAUDE.md files
// - Custom slash commands
// AFTER (v0.1.0) - No settings loaded by default
// To get the old behavior:
const
result
=
query
({
prompt:
"Hello"
,
options:
{
settingSources:
[
"user"
,
"project"
,
"local"
]
}
});
// Or load only specific sources:
const
result
=
query
({
prompt:
"Hello"
,
options:
{
settingSources:
[
"project"
]
// Only project settings
}
});
Why this changed:
Ensures SDK applications have predictable behavior independent of local filesystem configurations. This is especially important for:
CI/CD environments
- Consistent behavior without local customizations
Deployed applications
- No dependency on filesystem settings
Testing
- Isolated test environments
Multi-tenant systems
- Prevent settings leakage between users
Backward compatibility:
If your application relied on filesystem settings (custom slash commands, CLAUDE.md instructions, etc.), add
settingSources: ['user', 'project', 'local']
to your options.
​
Why the Rename?
The Claude Code SDK was originally designed for coding tasks, but it has evolved into a powerful framework for building all types of AI agents. The new name “Claude Agent SDK” better reflects its capabilities:
Building business agents (legal assistants, finance advisors, customer support)
Creating specialized coding agents (SRE bots, security reviewers, code review agents)
Developing custom agents for any domain with tool use, MCP integration, and more
​
Getting Help
If you encounter any issues during migration:
For TypeScript/JavaScript:
Check that all imports are updated to use
@anthropic-ai/claude-agent-sdk
Verify your package.json has the new package name
Run
npm install
to ensure dependencies are updated
For Python:
Check that all imports are updated to use
claude_agent_sdk
Verify your requirements.txt or pyproject.toml has the new package name
Run
pip install claude-agent-sdk
to ensure the package is installed
See the
Troubleshooting
guide for common issues.
​
Next Steps
Explore the
Agent SDK Overview
to learn about available features
Check out the
TypeScript SDK Reference
for detailed API documentation
Review the
Python SDK Reference
for Python-specific documentation
Learn about
Custom Tools
and
MCP Integration
Was this page helpful?
Yes
No
Best practices
Overview
Assistant
Responses are generated using AI and may contain mistakes.