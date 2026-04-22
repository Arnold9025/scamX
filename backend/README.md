# ScamX Backend

FastAPI + PostgreSQL backend for the ScamX scam detection app.

---

## Requirements

- Python 3.11+
- PostgreSQL

---

## Setup

**1. Create and activate the virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

```bash
cp .env.example .env
```

Edit `.env` and fill in your values:

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/scamx
SECRET_KEY=your-secret-key
```

**4. Run database migrations**

```bash
alembic upgrade head
```

**5. Start the development server**

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs at `http://localhost:8000/docs`.

---

## Project Structure

```
backend/
├── app/
│   ├── main.py               # App entry point, middleware, router registration
│   ├── core/
│   │   ├── config.py         # Settings loaded from .env
│   │   └── database.py       # Async SQLAlchemy engine, Base, get_db()
│   ├── api/
│   │   └── v1/
│   │       └── router.py     # All v1 route handlers
│   ├── models/               # SQLAlchemy ORM models (one file per table)
│   ├── schemas/              # Pydantic request/response schemas
│   └── services/             # Business logic, decoupled from routes
├── migrations/               # Alembic migration files
│   └── versions/
├── tests/
├── venv/
├── .env.example
├── alembic.ini
└── requirements.txt
```

---

## Adding a Feature

**New model** — create `app/models/thing.py`, import `Base` from `app.core.database`.

**New migration** — after adding a model, run:

```bash
alembic revision --autogenerate -m "add thing table"
alembic upgrade head
```

**New route group** — create `app/api/v1/thing.py` with an `APIRouter`, then register it in `app/api/v1/router.py`:

```python
from app.api.v1 import thing
router.include_router(thing.router, prefix="/things", tags=["things"])
```

**New service** — create `app/services/thing.py` with plain async functions, import into routes.

---

## Running Tests

```bash
pytest tests/
```

---

## Common Commands

| Task | Command |
|---|---|
| Start dev server | `uvicorn app.main:app --reload` |
| Create migration | `alembic revision --autogenerate -m "message"` |
| Apply migrations | `alembic upgrade head` |
| Rollback one step | `alembic downgrade -1` |
| Run tests | `pytest tests/` |
