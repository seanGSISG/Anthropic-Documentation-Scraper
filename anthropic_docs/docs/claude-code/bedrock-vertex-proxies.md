Source: https://docs.claude.com/en/docs/claude-code/bedrock-vertex-proxies
Last fetched: 2025-10-27T12:05:08.932459
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
Deployment
Enterprise deployment overview
Home
Developer Guide
API Reference
Claude Code
Model Context Protocol (MCP)
Resources
Release Notes
Getting started
Overview
Quickstart
Common workflows
Claude Code on the web
Build with Claude Code
Subagents
Plugins
Agent Skills
Output styles
Hooks
Headless mode
GitHub Actions
GitLab CI/CD
Model Context Protocol (MCP)
Troubleshooting
Claude Agent SDK
Migrate to Claude Agent SDK
Deployment
Overview
Amazon Bedrock
Google Vertex AI
Network configuration
LLM gateway
Development containers
Sandboxing
Administration
Advanced installation
Identity and Access Management
Security
Data usage
Monitoring
Costs
Analytics
Plugin marketplaces
Configuration
Settings
Visual Studio Code
JetBrains IDEs
Terminal configuration
Model configuration
Memory management
Status line configuration
Reference
CLI reference
Interactive mode
Slash commands
Checkpointing
Hooks reference
Plugins reference
Resources
Legal and compliance
On this page
Provider comparison
Cloud providers
Corporate infrastructure
Configuration overview
Using Bedrock with corporate proxy
Using Bedrock with LLM Gateway
Using Vertex AI with corporate proxy
Using Vertex AI with LLM Gateway
Authentication configuration
Choosing the right deployment configuration
Direct provider access
Corporate proxy
LLM Gateway
Debugging
Best practices for organizations
1. Invest in documentation and memory
2. Simplify deployment
3. Start with guided usage
4. Configure security policies
5. Leverage MCP for integrations
Next steps
This page provides an overview of available deployment options and helps you choose the right configuration for your organization.
​
Provider comparison
Feature
Anthropic
Amazon Bedrock
Google Vertex AI
Regions
Supported
countries
Multiple AWS
regions
Multiple GCP
regions
Prompt caching
Enabled by default
Enabled by default
Enabled by default
Authentication
API key
AWS credentials (IAM)
GCP credentials (OAuth/Service Account)
Cost tracking
Dashboard
AWS Cost Explorer
GCP Billing
Enterprise features
Teams, usage monitoring
IAM policies, CloudTrail
IAM roles, Cloud Audit Logs
​
Cloud providers
Amazon Bedrock
Use Claude models through AWS infrastructure with IAM-based authentication and AWS-native monitoring
Google Vertex AI
Access Claude models via Google Cloud Platform with enterprise-grade security and compliance
​
Corporate infrastructure
Enterprise Network
Configure Claude Code to work with your organization’s proxy servers and SSL/TLS requirements
LLM Gateway
Deploy centralized model access with usage tracking, budgeting, and audit logging
​
Configuration overview
Claude Code supports flexible configuration options that allow you to combine different providers and infrastructure:
Understand the difference between:
Corporate proxy
: An HTTP/HTTPS proxy for routing traffic (set via
HTTPS_PROXY
or
HTTP_PROXY
)
LLM Gateway
: A service that handles authentication and provides provider-compatible endpoints (set via
ANTHROPIC_BASE_URL
,
ANTHROPIC_BEDROCK_BASE_URL
, or
ANTHROPIC_VERTEX_BASE_URL
)
Both configurations can be used in tandem.
​
Using Bedrock with corporate proxy
Route Bedrock traffic through a corporate HTTP/HTTPS proxy:
Copy
# Enable Bedrock
export
CLAUDE_CODE_USE_BEDROCK
=
1
export
AWS_REGION
=
us-east-1
# Configure corporate proxy
export
HTTPS_PROXY
=
'https://proxy.example.com:8080'
​
Using Bedrock with LLM Gateway
Use a gateway service that provides Bedrock-compatible endpoints:
Copy
# Enable Bedrock
export
CLAUDE_CODE_USE_BEDROCK
=
1
# Configure LLM gateway
export
ANTHROPIC_BEDROCK_BASE_URL
=
'https://your-llm-gateway.com/bedrock'
export
CLAUDE_CODE_SKIP_BEDROCK_AUTH
=
1
# If gateway handles AWS auth
​
Using Vertex AI with corporate proxy
Route Vertex AI traffic through a corporate HTTP/HTTPS proxy:
Copy
# Enable Vertex
export
CLAUDE_CODE_USE_VERTEX
=
1
export
CLOUD_ML_REGION
=
us-east5
export
ANTHROPIC_VERTEX_PROJECT_ID
=
your-project-id
# Configure corporate proxy
export
HTTPS_PROXY
=
'https://proxy.example.com:8080'
​
Using Vertex AI with LLM Gateway
Combine Google Vertex AI models with an LLM gateway for centralized management:
Copy
# Enable Vertex
export
CLAUDE_CODE_USE_VERTEX
=
1
# Configure LLM gateway
export
ANTHROPIC_VERTEX_BASE_URL
=
'https://your-llm-gateway.com/vertex'
export
CLAUDE_CODE_SKIP_VERTEX_AUTH
=
1
# If gateway handles GCP auth
​
Authentication configuration
Claude Code uses the
ANTHROPIC_AUTH_TOKEN
for the
Authorization
header when needed. The
SKIP_AUTH
flags (
CLAUDE_CODE_SKIP_BEDROCK_AUTH
,
CLAUDE_CODE_SKIP_VERTEX_AUTH
) are used in LLM gateway scenarios where the gateway handles provider authentication.
​
Choosing the right deployment configuration
Consider these factors when selecting your deployment approach:
​
Direct provider access
Best for organizations that:
Want the simplest setup
Have existing AWS or GCP infrastructure
Need provider-native monitoring and compliance
​
Corporate proxy
Best for organizations that:
Have existing corporate proxy requirements
Need traffic monitoring and compliance
Must route all traffic through specific network paths
​
LLM Gateway
Best for organizations that:
Need usage tracking across teams
Want to dynamically switch between models
Require custom rate limiting or budgets
Need centralized authentication management
​
Debugging
When debugging your deployment:
Use the
claude /status
slash command
. This command provides observability into any applied authentication, proxy, and URL settings.
Set environment variable
export ANTHROPIC_LOG=debug
to log requests.
​
Best practices for organizations
​
1. Invest in documentation and memory
We strongly recommend investing in documentation so that Claude Code understands your codebase. Organizations can deploy CLAUDE.md files at multiple levels:
Organization-wide
: Deploy to system directories like
/Library/Application Support/ClaudeCode/CLAUDE.md
(macOS) for company-wide standards
Repository-level
: Create
CLAUDE.md
files in repository roots containing project architecture, build commands, and contribution guidelines. Check these into source control so all users benefit
Learn more
.
​
2. Simplify deployment
If you have a custom development environment, we find that creating a “one click” way to install Claude Code is key to growing adoption across an organization.
​
3. Start with guided usage
Encourage new users to try Claude Code for codebase Q&A, or on smaller bug fixes or feature requests. Ask Claude Code to make a plan. Check Claude’s suggestions and give feedback if it’s off-track. Over time, as users understand this new paradigm better, then they’ll be more effective at letting Claude Code run more agentically.
​
4. Configure security policies
Security teams can configure managed permissions for what Claude Code is and is not allowed to do, which cannot be overwritten by local configuration.
Learn more
.
​
5. Leverage MCP for integrations
MCP is a great way to give Claude Code more information, such as connecting to ticket management systems or error logs. We recommend that one central team configures MCP servers and checks a
.mcp.json
configuration into the codebase so that all users benefit.
Learn more
.
At Anthropic, we trust Claude Code to power development across every Anthropic codebase. We hope you enjoy using Claude Code as much as we do!
​
Next steps
Set up Amazon Bedrock
for AWS-native deployment
Configure Google Vertex AI
for GCP deployment
Configure Enterprise Network
for network requirements
Deploy LLM Gateway
for enterprise management
Settings
for configuration options and environment variables
Was this page helpful?
Yes
No
Migrate to Claude Agent SDK
Amazon Bedrock
Assistant
Responses are generated using AI and may contain mistakes.