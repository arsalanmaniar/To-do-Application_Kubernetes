# Data Model: AI-Powered Todo Dashboard - Extended

## Existing Models (Current State)

### User Entity (Already Implemented)
**Fields**:
- id (UUID, Primary Key)
- email (String, Unique, Required)
- hashed_password (String, Required)
- is_active (Boolean, Default: True)
- created_at (DateTime, Required)

**Validation**:
- Email must be valid email format
- Email must be unique across all users

**Relationships**:
- One-to-Many: User → Tasks

### Task Entity (Already Implemented)
**Fields**:
- id (UUID, Primary Key)
- title (String, Required)
- description (Text, Optional)
- completed (Boolean, Default: False)
- owner_id (String, Foreign Key to User, Required)
- created_at (DateTime, Required)
- updated_at (DateTime, Required)

**Validation**:
- Title must be between 1-255 characters
- Description limited to 2000 characters

**Relationships**:
- Many-to-One: Task → User (owner)

## New Models (Required for Phase III)

### Project Entity
**Fields**:
- id (UUID, Primary Key)
- name (String, Required)
- description (Text, Optional)
- owner_id (String, Foreign Key to User, Required)
- created_at (DateTime, Required)
- updated_at (DateTime, Required)

**Validation**:
- Name must be between 1-255 characters
- Description limited to 2000 characters

**Relationships**:
- Many-to-One: Project → User (owner)
- One-to-Many: Project → Tasks

### Team Entity
**Fields**:
- id (UUID, Primary Key)
- name (String, Required)
- description (Text, Optional)
- owner_id (String, Foreign Key to User, Required)
- created_at (DateTime, Required)
- updated_at (DateTime, Required)

**Validation**:
- Name must be between 1-255 characters
- Description limited to 2000 characters

**Relationships**:
- Many-to-One: Team → User (owner)
- Many-to-Many: Team ↔ Users (via membership table)

### TeamMembership Entity
**Fields**:
- id (UUID, Primary Key)
- team_id (UUID, Foreign Key to Team, Required)
- user_id (String, Foreign Key to User, Required)
- role (String: 'member', 'admin', Default: 'member')
- joined_at (DateTime, Required)

**Validation**:
- Role must be one of allowed values
- Combination of team_id and user_id must be unique

**Relationships**:
- Many-to-One: TeamMembership → Team
- Many-to-One: TeamMembership → User

### CalendarEvent Entity
**Fields**:
- id (UUID, Primary Key)
- title (String, Required)
- description (Text, Optional)
- start_time (DateTime, Required)
- end_time (DateTime, Required)
- all_day (Boolean, Default: False)
- owner_id (String, Foreign Key to User, Required)
- task_id (UUID, Foreign Key to Task, Optional)
- created_at (DateTime, Required)
- updated_at (DateTime, Required)

**Validation**:
- Start time must be before end time
- Title must be between 1-255 characters

**Relationships**:
- Many-to-One: CalendarEvent → User (owner)
- Many-to-One: CalendarEvent → Task (optional)

### Conversation Entity (For AI Integration)
**Fields**:
- id (UUID, Primary Key)
- title (String, Required)
- owner_id (String, Foreign Key to User, Required)
- created_at (DateTime, Required)
- updated_at (DateTime, Required)

**Validation**:
- Title must be between 1-255 characters

**Relationships**:
- Many-to-One: Conversation → User (owner)
- One-to-Many: Conversation → Messages

### Message Entity (For AI Integration)
**Fields**:
- id (UUID, Primary Key)
- conversation_id (UUID, Foreign Key to Conversation, Required)
- sender (String: 'user', 'ai', Required)
- content (Text, Required)
- created_at (DateTime, Required)

**Validation**:
- Content must be between 1-10000 characters

**Relationships**:
- Many-to-One: Message → Conversation