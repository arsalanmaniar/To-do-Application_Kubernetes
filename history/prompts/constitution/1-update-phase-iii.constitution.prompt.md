---
id: 1
title: "Update Phase III Constitution"
stage: constitution
date_iso: "2026-02-02"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "001-frontend-ui-fixes"
user: "user"
command: "/sp.constitution Update for Phase III (Spec-4)."
labels: ["constitution", "phase-iii", "spec-4"]
spec: null
ticket: null
adr: null
pr: null
files_yaml: |
  - .specify/memory/constitution.md
  - history/prompts/constitution/1-update-phase-iii.constitution.prompt.md
tests_yaml: []
---

# Prompt Text

```
Update for Phase III (Spec-4).

Context:
- Phase 3 folder is created by copying Phase 2
- All new development will happen inside Phase 3
- Spec-4 is now the active specification

Add / Update the constitution to enforce:

1. Development Rules
- Use Agentic Dev Stack only: Spec → Plan → Tasks → Implement
- No manual coding allowed
- All code must be generated via Claude Code / CLI
- Every change must trace back to an approved spec

2. Architecture Constraints
- Backend: FastAPI (stateless)
- AI Logic: OpenAI Agents SDK only
- MCP Server: Official MCP SDK only
- Database: Neon Serverless PostgreSQL via SQLModel
- Conversation state must persist in DB, server holds no memory

3. AI & MCP Rules
- AI agents can ONLY interact with tasks via MCP tools
- MCP tools must be stateless and DB-backed
- No direct DB access from agents outside MCP


4. Phase III Scope
- AI-powered Todo Chatbot
- Natural language task management
- Stateless chat endpoint with persistent history
- Resume conversations after server restart

5. Evaluation Criteria
- Spec compliance is mandatory
- Correct MCP tool usage
- Clean agent behavior mapping to user intent
- Friendly confirmations and graceful error handling

This constitution overrides previous phase rules where conflicts exist.
```

# Response Text

Updated the project constitution to version 2.0.0 for Phase III (Spec-4) with the following changes:

- Updated core principles to reflect Agentic Dev Stack Only, No Manual Coding, Spec Traceability, MCP Security Rules, Architecture Constraints, and AI-MCP Integration
- Added technology, process, and security constraints specific to Phase III requirements
- Added new sections for Phase III Scope, AI & MCP Rules, and Evaluation Criteria
- Updated governance section to reflect the new AI-powered Todo Chatbot focus
- Created a sync impact report showing version change from 1.1.0 to 2.0.0
- Included all required rules about MCP tools, stateless architecture, and AI integration

The updated constitution now enforces all the specified requirements for Phase III development.

# Outcome

Successfully updated the constitution to enforce the new Phase III development rules, architecture constraints, AI & MCP rules, scope requirements, and evaluation criteria as requested.

# Evaluation

The constitution update successfully incorporates all requested changes:
- ✅ Development Rules (Agentic Dev Stack, no manual coding, spec traceability)
- ✅ Architecture Constraints (FastAPI, OpenAI Agents SDK, MCP SDK, Neon PostgreSQL)
- ✅ AI & MCP Rules (agents only via MCP tools, stateless tools, no direct DB access)
- ✅ Phase III Scope (AI chatbot, natural language, persistent history)
- ✅ Evaluation Criteria (compliance, MCP usage, agent behavior)
- ✅ Version properly incremented to 2.0.0 as this is a major update