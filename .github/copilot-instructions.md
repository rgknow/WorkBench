# WorkBench - AI Coding Agent Instructions

## Architecture Overview
This is a **NanoSkool Olympiad** monorepo with four independent services designed for educational platform development:

- **`backend/`** - FastAPI service (port 8000) for assessments and progress tracking
- **`dashboard/`** - React/Vite frontend (port 5173) with minimal TypeScript setup
- **`edx_xblock/`** - EdX XBlock plugin for LMS integration 
- **`maker_workbench/`** - Static Blockly visual programming interface

## Key Patterns & Conventions

### Backend (FastAPI)
- Uses Pydantic models for API contracts (see `AssessmentItem`, `Submission` in `main.py`)
- CORS configured specifically for localhost:5173 dashboard integration
- Follows simple CRUD pattern: `/assessment/items`, `/assessment/submit`, `/progress/{user_id}`
- Direct uvicorn execution in `main.py` for development (not separate ASGI config)

### Frontend (React/Vite)
- Minimal setup with direct fetch calls to backend (no axios/query libraries)
- TypeScript strict mode enabled, targeting ES2020
- Uses React 18 with `createRoot` pattern in `main.tsx`
- Development server hardcoded to port 5173 in `vite.config.ts`

### XBlock Integration
- Implements EdX XBlock pattern with `student_view()` and JSON handlers
- Uses jQuery (EdX requirement) for DOM manipulation in JavaScript fragments
- State management via XBlock fields: `Scope.settings` vs `Scope.user_state`
- Handler URLs generated via `runtime.handlerUrl()` pattern

## Development Workflows

### Local Development Commands
```bash
# Backend (from backend/ directory)
python -m pip install -e .
python app/main.py  # Direct execution, not uvicorn command

# Dashboard (from dashboard/ directory)  
npm install
npm run dev  # Vite dev server

# Maker Workbench
# Open maker_workbench/index.html directly in browser
```

### Package Management
- Backend uses `pyproject.toml` with setuptools (not Poetry/pip-tools)
- Dependencies include data science stack (numpy, pandas) for assessment scoring
- XBlock has separate `pyproject.toml` with XBlock>=1.8.0 requirement

## Cross-Service Integration

### Backend ↔ Dashboard Communication
- Dashboard fetches from hardcoded `http://localhost:8000` endpoints
- Backend serves mock data with realistic structure (skills radar, creativity index)
- CORS middleware configured for development ports only

### Data Models
- Assessment items support both MCQ (`options` array) and short answer (`type` field)
- Progress tracking uses 6-skill radar: Communication, Creativity, Collaboration, Coding, Critical Thinking, Care
- User identification via simple string `user_id` (no authentication layer)

## Project-Specific Considerations

### EdX Integration
- XBlock requires running Open edX devstack for testing
- Uses Fragment pattern for HTML/JS/CSS assembly
- jQuery dependency inherited from EdX platform requirements

### Educational Context
- Assessment scoring includes partial credit logic (0.5 for partial answers)
- Progress visualization designed for student skill development tracking
- Blockly workspace exposed globally (`window.workspace`) for external integrations

## File Structure Patterns
- Each service has independent `README.md` with specific setup instructions
- Configuration files follow standard conventions (no custom build tools)
- Python packages use `-` naming (nanoskool-backend) vs `_` for modules (nanoskool_xblock)