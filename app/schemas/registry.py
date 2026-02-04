from __future__ import annotations

from typing import Any
from pydantic import BaseModel, Field


class ToolCreate(BaseModel):
    name: str = Field(min_length=2, max_length=64, pattern=r"^[a-zA-Z0-9_\-]+$")
    description: str
    schema: dict[str, Any]


class ToolOut(BaseModel):
    name: str
    version: int
    description: str
    schema: dict[str, Any]
