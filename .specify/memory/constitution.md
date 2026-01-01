<!--
Sync Impact Report:
- Version change: 1.0.0 → 1.1.0
- Modified principles: Added 5 specific principles for Todo app
- Added sections: Core Principles, Key Standards, Constraints, Success Criteria
- Removed sections: Template placeholders
- Templates requiring updates: N/A (new constitution)
- Follow-up TODOs: None
-->
# Evolution of Todo – Phase I (In-Memory Python CLI App) Constitution

## Core Principles

### Spec-Driven Development
All features must be designed using specs before code generation. Every implementation must be traceable back to a specification document that defines inputs, outputs, expected behavior, edge cases, and dependencies.

### Accuracy
Ensure that all feature behaviors match the specifications. Code generation must follow the design exactly without deviation, and all functionality must be verified against the original spec requirements.

### Clarity
Code and CLI outputs must be understandable and user-friendly. Both the application interface and the underlying code must be clear to users and maintainers, with proper documentation and intuitive design.

### Clean Code
Follow Python best practices, modular design, and maintainable structure. Code must adhere to clean code principles including proper naming conventions, modularity, and readability.

### Reproducibility
Every spec should be traceable and implementable via Claude Code. All specifications must be detailed enough to be converted into working code through automated processes.

## Key Standards

### Folder Structure
- `/src` : All Python source code
- `/specs_history` : All specification files generated
- `README.md` : Setup and usage instructions
- `CLAUDE.md` : Instructions for using Claude Code
- `constitution.md` : This constitution

### Technology Requirements
- Python version: 3.13+
- Task model: Each task must have a unique ID, title, description, and completed status

### Feature Implementation Requirements
- Add Task – Add a new todo item
- Delete Task – Remove tasks by ID
- Update Task – Modify task details
- View Task List – List all tasks with status indicators
- Mark as Complete – Toggle task completion status

### Code Architecture
- CLI interactions should be in `main.py` only
- All logic must be encapsulated in classes (Task, TodoManager)
- Each feature must have a corresponding spec file in `/specs_history`

## Constraints

### Code Generation
- You cannot write code manually; all code must be generated/refined using Claude Code from specs
- Each spec must define inputs, outputs, expected behavior, edge cases, and dependencies
- Features must be independently testable via CLI

### Code Quality
- Code must follow clean code principles (naming conventions, modularity, readability)
- All implementations must be traceable to specifications

## Success Criteria

### Functional Requirements
- All five basic features are fully functional in CLI
- Specs are complete and stored in `/specs_history`
- Generated code matches the specs without manual intervention

### Documentation Requirements
- README.md and CLAUDE.md provide clear setup and usage instructions
- Application demonstrates adding, viewing, updating, deleting, and marking tasks as complete

## Governance

This constitution serves as the governing document for all development activities in the Todo app project. All code generation, feature implementation, and architectural decisions must align with these principles. Amendments to this constitution require explicit approval and documentation of the changes and their impact on existing specifications and implementations.

**Version**: 1.1.0 | **Ratified**: 2025-12-29 | **Last Amended**: 2025-12-29