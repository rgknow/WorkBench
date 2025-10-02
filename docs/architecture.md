# Architecture Overview

- Backend: FastAPI (port 8000)
- Dashboard: React + Vite (port 5173), proxied via Nginx to backend `/api`
- XBlock: EdX plugin providing course widgets
- Maker Workbench: Static Blockly, future device bridges
