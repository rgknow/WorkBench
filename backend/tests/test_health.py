import asyncio
import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_health_and_progress():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        r = await ac.get("/health")
        assert r.status_code == 200
        assert r.json().get("status") == "ok"

        r2 = await ac.get("/progress/demo")
        assert r2.status_code == 200
        body = r2.json()
        assert body.get("user_id") == "demo"
