# Agent Skill Registry

Register tool schemas, track versions, and browse the latest definitions.

## Why this project

As you build agent systems, tool interfaces drift. A registry with versioning + schema storage keeps your tools consistent and makes it easier to generate clients and validate calls.

## Inspiration / Sources

- JSON Schema — https://json-schema.org/
- FastAPI docs — https://fastapi.tiangolo.com/

## Architecture

- FastAPI backend: `app/` (app factory + routers + services + core domain)
- Streamlit UI: `app/web/streamlit_app.py`

## Run (dev)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
```

Terminal A (API):

```bash
API_PORT=8202 ./scripts/dev_api.sh
```

Terminal B (UI):

```bash
UI_API_URL=http://127.0.0.1:8202 streamlit run app/web/streamlit_app.py --server.port 8602
```

## Smoke test

```bash
curl -s http://127.0.0.1:8202/api/health | python3 -m json.tool
```

## Roadmap (Next steps)

- Add persistence (SQLite) where applicable
- Add auth + rate limiting
- Add background jobs + queue for long-running tasks
- Add Docker + deployment target
