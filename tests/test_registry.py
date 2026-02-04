from app.core.registry import ToolRegistry


def test_versioning() -> None:
    reg = ToolRegistry()
    t1 = reg.register('x', 'd', {'a': 1})
    t2 = reg.register('x', 'd2', {'a': 2})
    assert t1.version == 1
    assert t2.version == 2
    assert reg.latest('x').schema['a'] == 2
