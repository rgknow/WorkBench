# NanoSkool AI LMS — Code → Chip → PCB → CAD → Product → Launch → Scale

Mono-repo powering the NanoSkool Olympiad and AI LMS.

Packages:
- `backend/` — FastAPI app + OpenAPI
- `dashboard/` — React (Vite) dashboard
- `edx_xblock/` — EdX XBlock starter
- `maker_workbench/` — Static Blockly page

## Quick Start (local)

Using Docker Compose:

```bash
docker compose up -d --build
# FE: http://localhost:5173  |  API: http://localhost:8000/docs
```

Manual:

```bash
# Backend
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/app/main.py

# Frontend
cd dashboard && npm install && npm run dev
```

## Branch & Fork Model

Default branch: `develop` (integration). Production: `main` (protected). Create `feature/<scope>-<desc>` branches and open PRs to `develop`.

## Deployment

See `docs/deployment_guide.md` for server steps and Nginx reverse proxying.
