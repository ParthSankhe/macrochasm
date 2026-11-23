# Architecture decisions

A short log of significant choices, why they were made, and what was traded off.

---

## 001: FastAPI + PostgreSQL, no extra infrastructure

**Decision:** A single FastAPI service backed by PostgreSQL. No message queues, caches or microservices.

**Why:** The dataset (hundreds of thousands of products, ~10 metrics each) fits comfortably in one Postgres instance, and ratio queries are simple SQL. Extra infrastructure would add operational cost without solving a real problem at this scale.

**Revisit if:** Query latency or price-refresh volume outgrows a single database.

---

## 002: Wide `products` table instead of long nutrient rows

**Decision:** USDA ships nutrients in long format (one row per product–nutrient pair). The ETL pivots this into one row per product with a column per nutrient.

**Why:** Every search divides one column by another within the same product. In a wide table that is `protein_g / energy_kcal`; in a long table it needs a self-join per metric.

**Trade-off:** Adding a new nutrient requires a migration. Acceptable, because the metric set is small and changes rarely.

---

## 003: Store nutrients per 100 g

**Decision:** Keep USDA's per-100 g values instead of converting to per-serving.

**Why:** Serving sizes are set by manufacturers and vary widely; per-100 g values make ratios directly comparable. Serving size is kept separately for display and per-serving cost.
