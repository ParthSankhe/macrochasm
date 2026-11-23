from fastapi import FastAPI

app = FastAPI(
    title="Macrochasm API",
    description="Search packaged foods by nutrient and cost ratios.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness check used by CI and deployment platforms."""
    return {"status": "ok"}
