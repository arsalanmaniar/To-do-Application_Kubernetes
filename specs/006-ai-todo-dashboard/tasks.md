# Tasks: AI-Powered Todo Dashboard

## Phase 1: Setup

- [ ] T001 Create project structure documentation in specs/006-ai-todo-dashboard/
- [ ] T002 Set up development environment with proper Python/Node versions
- [ ] T003 Configure database connection to Neon Serverless PostgreSQL

## Phase 2: Foundational

- [X] T004 [P] Create Project model in backend/app/models/project.py
- [X] T005 [P] Create Team model in backend/app/models/team.py
- [X] T006 [P] Create TeamMembership model in backend/app/models/team_membership.py
- [X] T007 [P] Create CalendarEvent model in backend/app/models/calendar_event.py
- [X] T008 [P] Create Conversation model in backend/app/models/conversation.py
- [X] T009 [P] Create Message model in backend/app/models/message.py
- [X] T010 [P] Create Project schemas in backend/app/schemas/project.py
- [X] T011 [P] Create Team schemas in backend/app/schemas/team.py
- [X] T012 [P] Create CalendarEvent schemas in backend/app/schemas/calendar_event.py
- [X] T013 [P] Create Conversation schemas in backend/app/schemas/conversation.py
- [X] T014 [P] Create Message schemas in backend/app/schemas/message.py

## Phase 3: User Story 1 - User Registration and Authentication (Priority: P1)

- [ ] T015 [US1] Verify existing auth endpoints work properly in backend/api/v1/auth.py
- [ ] T016 [US1] Verify password visibility toggle functionality in frontend/src/app/auth/sign-in/page.tsx
- [ ] T017 [US1] Verify password visibility toggle functionality in frontend/src/app/auth/sign-up/page.tsx
- [ ] T018 [US1] Test user registration flow with existing UI
- [ ] T019 [US1] Test user login flow with existing UI
- [ ] T020 [US1] Verify redirect to dashboard after successful login

## Phase 4: User Story 2 - Todo Management with AI Features (Priority: P1)

- [ ] T021 [US2] Verify existing task CRUD operations work properly
- [ ] T022 [US2] Create task service extensions for AI integration in backend/app/services/task_service.py
- [X] T023 [US2] Prepare AI integration layer in backend/app/services/ai_service.py
- [ ] T024 [US2] Update task endpoints to support AI parsing in backend/app/api/v1/endpoints/tasks.py
- [X] T025 [US2] Create MCP server structure in backend/app/mcp/server.py
- [X] T026 [US2] Create MCP task tools in backend/app/mcp/tools/task_tools.py

## Phase 5: User Story 3 - Dashboard Navigation (Priority: P2)

- [X] T027 [P] [US3] Create Project service in backend/app/services/project_service.py
- [X] T028 [P] [US3] Create Team service in backend/app/services/team_service.py
- [X] T029 [P] [US3] Create CalendarEvent service in backend/app/services/calendar_service.py
- [X] T030 [US3] Create Project endpoints in backend/app/api/v1/endpoints/projects.py
- [X] T031 [US3] Create Team endpoints in backend/app/api/v1/endpoints/teams.py
- [X] T032 [US3] Create CalendarEvent endpoints in backend/app/api/v1/endpoints/calendar.py
- [X] T033 [US3] Connect Calendar page to backend API in frontend/src/app/calendar/page.tsx
- [X] T034 [US3] Connect Projects page to backend API in frontend/src/app/projects/page.tsx
- [X] T035 [US3] Connect Team page to backend API in frontend/src/app/team/page.tsx
- [ ] T036 [US3] Test navigation between dashboard sections

## Phase 6: User Story 4 - Password Visibility Toggle (Priority: P2)

- [ ] T037 [US4] Verify password toggle functionality works correctly in sign-in form
- [ ] T038 [US4] Verify password toggle functionality works correctly in sign-up form
- [ ] T039 [US4] Test accessibility of password visibility toggle feature

## Phase 7: AI Preparation and MCP Integration

- [X] T040 Create Conversation endpoints in backend/app/api/v1/endpoints/conversations.py
- [X] T041 Create Message endpoints in backend/app/api/v1/endpoints/messages.py
- [X] T042 Create MCP conversation tools in backend/app/mcp/tools/conversation_tools.py
- [X] T043 Set up MCP configuration in backend/config/mcp_config.py
- [X] T044 Create MCP middleware in backend/app/middleware/mcp_middleware.py
- [X] T045 Update main application to include MCP routes in backend/main.py

## Phase 8: Polish & Cross-Cutting Concerns

- [X] T046 Update API documentation with new endpoints
- [X] T047 Add error handling for new features
- [X] T048 Add logging for new services
- [X] T049 Update frontend API client to support new endpoints in frontend/src/lib/api.ts
- [X] T050 Test complete user flow from registration to dashboard navigation
- [X] T051 Verify database migrations work for new models
- [X] T052 Update environment variables documentation

## Phase 9: AI Chatbot Feature (Priority: P1)

- [X] T053 [P] Create ChatMessage component in frontend/src/components/chat/ChatMessage.tsx
- [X] T054 [P] Create ChatInput component in frontend/src/components/chat/ChatInput.tsx
- [X] T055 [P] Create Chatbot component in frontend/src/components/chat/Chatbot.tsx
- [X] T056 [P] Create FloatingChatButton component in frontend/src/components/chat/FloatingChatButton.tsx
- [X] T057 [P] Create chat API endpoint in backend/app/api/v1/endpoints/chat.py
- [X] T058 [P] Enhance AI service with chat functionality in backend/app/services/ai_service.py
- [X] T059 [P] Create chat API client in frontend/src/lib/api/chat-api.ts
- [X] T060 [P] Create chat page in frontend/src/app/chat/page.tsx
- [X] T061 [P] Integrate floating chat button globally in frontend/src/app/layout.tsx
- [X] T062 [P] Update main application to include chat routes in backend/main.py

## Dependencies

1. User Story 1 (Authentication) - Foundation for all other stories
2. User Story 2 (Task Management) - Depends on User Story 1
3. User Story 3 (Dashboard Navigation) - Depends on User Story 1 and foundational models
4. User Story 4 (Password Toggle) - Depends on User Story 1 (already implemented)

## Parallel Execution Examples

- Models can be created in parallel (T004-T009)
- Schemas can be created in parallel (T010-T013)
- Services can be created in parallel after models exist (T027-T029)
- Endpoints can be created in parallel after services exist (T030-T032)

## Implementation Strategy

Start with foundational models and schemas (Phase 1-2) to establish the data layer, then implement user stories in priority order. Each user story should be independently testable and provide value to users. The AI preparation phase sets up infrastructure for future enhancements.