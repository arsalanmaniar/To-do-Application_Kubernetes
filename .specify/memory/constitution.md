<!--
SYNC IMPACT REPORT:
Version change: 1.1.0 → 2.0.0
Modified principles: Spec-First Development → Agentic Dev Stack Only, Agentic Purity → No Manual Coding, Determinism → Spec Traceability, Security-by-Design → MCP Security Rules, Separation of Concerns → Architecture Constraints, Stateless Architecture → AI-MCP Integration
Added sections: Phase III Scope, AI & MCP Rules, Evaluation Criteria
Removed sections: None
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: RATIFICATION_DATE needs to be set to original adoption date
-->

# AI-Powered Todo Chatbot Phase III Constitution

## Core Principles

### Agentic Dev Stack Only
Use Agentic Dev Stack only: Spec → Plan → Tasks → Implement. No implementation before a written and approved specification. All code must be generated via Claude Code prompts following the Specify → Plan → Implement → Review workflow with zero manual coding.

### No Manual Coding
No manual coding allowed. All code must be generated via Claude Code / CLI. Changes only allowed via spec revision or re-generation through Claude Code.

### Spec Traceability
Every change must trace back to an approved spec. Same spec must always produce functionally equivalent output. Every feature must map directly to a written spec requirement. Spec language must be clear, unambiguous, and implementation-agnostic.

### MCP Security Rules
AI agents can ONLY interact with tasks via MCP tools. MCP tools must be stateless and DB-backed. No direct DB access from agents outside MCP. Authentication, authorization, and data isolation enforced at every layer. Every API endpoint must enforce authentication and user ownership. All data access must be filtered by authenticated user ID.

### Architecture Constraints
Backend: FastAPI (stateless), AI Logic: OpenAI Agents SDK only, MCP Server: Official MCP SDK only, Database: Neon Serverless PostgreSQL via SQLModel. Frontend uses Next.js 16+ (App Router only), Authentication uses Better Auth (JWT-based). Conversation state must persist in DB, server holds no memory.

### AI-MCP Integration
AI agents can ONLY interact with tasks via MCP tools. MCP tools must be stateless and DB-backed. No direct DB access from agents outside MCP. Backend must remain stateless and JWT-driven. All API routes require valid JWT tokens. Requests without valid JWT return 401 Unauthorized. JWT must be signed using shared secret and time-limited (expiry enforced).

## Additional Constraints

Technology Constraints:
- Backend: FastAPI (stateless)
- AI Logic: OpenAI Agents SDK only
- MCP Server: Official MCP SDK only
- Database: Neon Serverless PostgreSQL via SQLModel
- Frontend: Next.js 16+ (App Router only)
- Authentication: Better Auth (JWT-based)
- Spec System: Spec-Kit Plus
- Development Style: CLI-first, no GUI-based manual setup

Process Constraints:
- Use Agentic Dev Stack only: Spec → Plan → Tasks → Implement
- No manual coding allowed
- No direct edits to generated code
- All code must be generated via Claude Code / CLI
- Every change must trace back to an approved spec
- Changes only allowed via:
  - Spec revision
  - Re-generation through Claude Code
- Each phase must follow:
  Specify → Plan → Tasks → Implement

Security Constraints:
- AI agents can ONLY interact with tasks via MCP tools
- MCP tools must be stateless and DB-backed
- No direct DB access from agents outside MCP
- All API routes require valid JWT tokens
- Requests without valid JWT return 401 Unauthorized
- JWT must be:
  - Signed using shared secret
  - Time-limited (expiry enforced)
- Backend must independently verify JWT
- No hardcoded secrets; all secrets via environment variables
- REST API must follow HTTP standards (status codes, verbs, idempotency)
- Database schema must be migration-safe and reproducible

## Phase III Scope

- AI-powered Todo Chatbot
- Natural language task management
- Stateless chat endpoint with persistent history
- Resume conversations after server restart
- Conversation state must persist in DB, server holds no memory

## AI & MCP Rules

- AI agents can ONLY interact with tasks via MCP tools
- MCP tools must be stateless and DB-backed
- No direct DB access from agents outside MCP
- MCP tools must be stateless and DB-backed
- Conversation state must persist in DB, server holds no memory
- AI Logic: OpenAI Agents SDK only
- MCP Server: Official MCP SDK only

## Development Workflow

Key Standards:
- Use Agentic Dev Stack only: Spec → Plan → Tasks → Implement
- Every feature must map directly to a written spec requirement
- Every API endpoint must:
  - Enforce authentication
  - Enforce user ownership
- All data access must be filtered by authenticated user ID
- No hardcoded secrets; all secrets via environment variables
- REST API must follow HTTP standards (status codes, verbs, idempotency)
- Database schema must be migration-safe and reproducible
- Spec language must be clear, unambiguous, and implementation-agnostic
- Conversation state must persist in DB, server holds no memory
- AI agents can ONLY interact with tasks via MCP tools

## Evaluation Criteria

- Spec compliance is mandatory
- Correct MCP tool usage
- Clean agent behavior mapping to user intent
- Friendly confirmations and graceful error handling
- Stateless chat endpoint with persistent history
- Resume conversations after server restart

## Governance

Objective: Transform a console-based Todo application into a modern, multi-user, production-ready AI-powered Todo Chatbot using a fully Spec-Driven and Agentic Development workflow (Claude Code + Spec-Kit Plus), with zero manual coding. All PRs/reviews must verify compliance with these principles. Complexity must be justified. Use CLAUDE.md for runtime development guidance. This constitution overrides previous phase rules where conflicts exist.

**Version**: 2.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-02-02