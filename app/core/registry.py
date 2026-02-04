from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Tool:
    name: str
    version: int
    description: str
    schema: dict[str, Any]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, list[Tool]] = {}

    def register(self, name: str, description: str, schema: dict[str, Any]) -> Tool:
        versions = self._tools.setdefault(name, [])
        v = len(versions) + 1
        tool = Tool(name=name, version=v, description=description, schema=schema)
        versions.append(tool)
        return tool

    def latest(self, name: str) -> Tool | None:
        versions = self._tools.get(name) or []
        return versions[-1] if versions else None

    def list_latest(self) -> list[Tool]:
        out: list[Tool] = []
        for name, versions in self._tools.items():
            if versions:
                out.append(versions[-1])
        return sorted(out, key=lambda t: t.name)
