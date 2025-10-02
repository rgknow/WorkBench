# NanoSkool AI LMS — Code → Chip → PCB → CAD → Product → Launch → Scale

Mono-repo powering the NanoSkool Global Creativity & STEAM Olympiad and AI LMS.

## Features
- FastAPI backend with assessment items, submissions, and progress metrics
- React (Vite) dashboard with configurable API base and Nginx proxy
- EdX XBlock starter for LMS integration
- Maker Workbench (Blockly) for block coding experiments
- Dockerized development with Compose and production-ready CI to build/publish images

## System architecture
See `docs/architecture.md` for diagrams. High-level:
- Backend (FastAPI) on port 8000 exposes OpenAPI `/docs`
- Dashboard (Vite) on port 5173 proxies `/api` → backend in dev and Nginx runtime
- XBlock package for EdX LMS embeds a simple prompt + save handler
- Maker Workbench is a static page embedding Blockly (future: transpile/bridge)

## API summary
See `docs/api_reference.md` for details:
- GET `/health` → `{ status: "ok" }`
- GET `/assessment/items` → list of items (MCQ/short answer)
- POST `/assessment/submit` → `{ ok, score }` (placeholder scoring)
- GET `/progress/{user_id}` → `{ user_id, creativity_index, skills }`

## Quick start (local)

Using Docker Compose:

```bash
docker compose up -d --build
# FE: http://localhost:5173  |  API: http://localhost:8000/docs
```

Manual dev:

```bash
# Backend
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/app/main.py

# Frontend
cd dashboard && npm install && npm run dev
```

## Deployment
Copy-pasteable server steps are in `docs/deployment_guide.md`.

## CI/CD
- GitHub Actions runs on PRs and pushes to `develop`/`main`, and on tags `v*`
- Jobs: backend (lint/tests), frontend (typecheck/build), docker (multi-arch build/push to GHCR)
- Images: `ghcr.io/<owner>/<repo>-backend` and `ghcr.io/<owner>/<repo>-dashboard`

## Branching model
- Default branch: `develop` (integration)
- Production: `main` (protected)
- Feature branches: `feature/<scope>-<desc>` → PR to `develop`
- Release tags: `vMAJOR.MINOR.PATCH` trigger image publishing

## Repo layout
- `backend/` — FastAPI app + tests
- `dashboard/` — React (Vite) + Nginx
- `edx_xblock/` — EdX XBlock starter
- `maker_workbench/` — Static Blockly page
- `docs/` — Architecture/API/Deployment guides

## Governance & security
See `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODEOWNERS`, and `LICENSE`.
