from __future__ import annotations

from typing import Any

from app.core.registry import ToolRegistry

_registry = ToolRegistry()


def register_tool(name: str, description: str, schema: dict[str, Any]):
    return _registry.register(name=name, description=description, schema=schema)


def list_tools():
    return _registry.list_latest()


def get_latest(name: str):
    return _registry.latest(name)
