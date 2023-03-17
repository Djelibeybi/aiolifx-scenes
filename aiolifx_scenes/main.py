"""Main module."""
from __future__ import annotations

import asyncio
import json
import logging
import os
from typing import Any

import httpx
from httpx_auth import HeaderApiKey

_LOGGER = logging.getLogger(__name__)

LIFX_URL = "https://api.lifx.com/v1/scenes"
TIMEOUT = 10.0


async def async_get_scenes(token: str) -> dict[str, Any] | None:
    """Return all scenes linked to the provided token."""
    auth_token = HeaderApiKey(f"Bearer {token}", header_name="Authorization")

    async with httpx.AsyncClient(auth=auth_token, timeout=TIMEOUT) as client:
        resp = await client.get(LIFX_URL)
        try:
            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as exc:
            _LOGGER.error("Error response %s from %s", exc.response.status_code, exc.request.url)
            return None


def get_scenes(token: str) -> dict[str, Any] | None:
    """Start an async task to return the scenes."""
    scenes = asyncio.run(async_get_scenes(token))
    return scenes


def __cli__():
    """Get the scene data and output in JSON format on the command-line."""
    token = os.getenv("LIFX_API_TOKEN", None)
    if token is None:
        print("Error: LIFX_API_TOKEN environment variable not set.")
        exit(1)

    scenes_json = json.dumps(get_scenes(token))
    print(scenes_json)
