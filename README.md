# Macrochasm

**A search engine for packaged foods by *ratios* of macros and cost. (protein per calorie, cost per gram of fibre, etc.)

> Find chips with more than 2 g of protein per 30 kcal.
> Find ready-to-eat foods with more than 5 g of fiber per dollar.
> Rank every yogurt by protein per dollar.

Nutrition labels tell you what's in one serving. Macrochasm answers the question shoppers actually have: *which product gives me the most of what I want, for the least of what I don't?*

> **Status:** 🚧 In active development. See the [roadmap](#roadmap) for progress.

---

## Workflow

1. **Ingest:** An ETL pipeline loads the USDA FoodData Central *Branded Foods* dataset (packaged products with label nutrition and UPC codes), deduplicates label versions, and pivots nutrients into a query-friendly table.
2. **Price:** Store prices are fetched from the Kroger Developer API and joined to products on normalized GTIN/UPC codes.
3. **Search:** Any metric can be divided by any other (protein per kcal, fiber per $, kcal per gram), then filtered and sorted.
4. **Rank sensibly:** Results are scored *relative to their category*, so a high-protein chip surfaces in a chips search instead of everything losing to whey protein powder.

## Metrics

| Metric | Unit |
|---|---|
| Energy | kcal |
| Protein | g |
| Fiber | g |
| Price | USD |
| Carbohydrates, sugars, added sugars | g |
| Total fat, saturated fat | g |
| Sodium | mg |

All nutrient values are stored per 100 g, so ratios are directly comparable across products.

## Tech stack

| Layer | Tools |
|---|---|
| API | Python 3.12, FastAPI, Pydantic |
| Database | PostgreSQL 16 + pgvector, SQLAlchemy 2.0, Alembic |
| Data pipeline | Polars |
| Frontend | Next.js, TypeScript, Tailwind CSS *(planned)* |
| Tooling | uv, Ruff, pytest, pre-commit |
| DevOps | Docker Compose, GitHub Actions CI |

Design decisions and their trade-offs are recorded in [`docs/decisions.md`](docs/decisions.md).

## Project structure

```
macrochasm/
├── backend/
│   ├── app/            FastAPI application
│   ├── tests/          pytest suite
│   └── pyproject.toml
├── docs/decisions.md   architecture decision log
├── docker-compose.yml  local PostgreSQL
└── .github/workflows/  CI
```

## Running locally

Requires [Docker](https://docs.docker.com/get-docker/) and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/<your-username>/macrochasm.git
cd macrochasm
cp .env.example .env

docker compose up -d          # start PostgreSQL

cd backend
uv sync                       # install dependencies
uv run uvicorn app.main:app --reload
```

The API is then available at http://localhost:8000, with interactive docs at http://localhost:8000/docs.

Run the checks:

```bash
cd backend
uv run ruff check .
uv run pytest
```

## Roadmap

- [x] Project scaffold, CI, local database
- [ ] ETL: load USDA Branded Foods into PostgreSQL
- [ ] `/search` endpoint: ratio queries with filters
- [ ] Kroger API price integration
- [ ] Category-relative ranking and Pareto-optimal results
- [ ] Semantic search with pgvector
- [ ] Next.js frontend
- [ ] Deployment

## Data sources

- [USDA FoodData Central](https://fdc.nal.usda.gov/): Branded Foods dataset (public domain)
- [Kroger Developer API](https://developer.kroger.com/): product prices

## License

[MIT](LICENSE)
