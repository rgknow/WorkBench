# Deployment Guide

This guide describes how to build and deploy the NanoSkool WorkBench stack with Docker Compose on a single Linux server.

## Prerequisites
- Linux host (Ubuntu 22.04+)
- Docker and Docker Compose (v2)
- 80/443 open in firewall if exposing the UI

## One-time server setup
```
# Install Docker
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker "$USER"
# Log out/in to apply group membership
```

## Clone and run
```
# Clone repo
git clone https://github.com/<your-org>/WorkBench.git
cd WorkBench

# Build and start services
docker compose up -d --build

# Verify
curl -s http://localhost:8000/health
```

- Frontend: http://<server-ip>:5173
- API docs: http://<server-ip>:8000/docs

## Configuration
- Dashboard API base URL: `dashboard/.env.example` (use `VITE_API_BASE` for non-proxy mode)
- Nginx (dashboard image) proxies `/api` → `backend:8000`

## Logs and updates
```
docker compose logs -f backend
docker compose logs -f dashboard

docker compose pull && docker compose up -d --build
```

## Production hardening (next steps)
- Put nginx/Traefik/Caddy in front with TLS (443)
- Add Postgres/Redis for stateful features
- Configure CI/CD to build and push images to a registry
