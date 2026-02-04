from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas.registry import ToolCreate, ToolOut
from app.services.registry_service import get_latest, list_tools, register_tool

router = APIRouter()


@router.post('/tools', response_model=ToolOut)
def create_tool(req: ToolCreate) -> ToolOut:
    t = register_tool(req.name, req.description, req.schema)
    return ToolOut(**t.__dict__)


@router.get('/tools', response_model=list[ToolOut])
def tools() -> list[ToolOut]:
    return [ToolOut(**t.__dict__) for t in list_tools()]


@router.get('/tools/{name}', response_model=ToolOut)
def tool(name: str) -> ToolOut:
    t = get_latest(name)
    if not t:
        raise HTTPException(404, 'tool not found')
    return ToolOut(**t.__dict__)
