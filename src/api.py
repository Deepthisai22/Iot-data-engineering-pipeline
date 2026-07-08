from fastapi import FastAPI
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

from src.config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD


app = FastAPI(
    title="Nectar IoT Data API",
    description="API for IoT Asset Monitoring",
    version="1.0"
)

encoded_password = quote_plus(DB_PASSWORD)

engine = create_engine(
    f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

@app.get("/")
def home():
    return {"message": "Welcome to Nectar IoT Data API"}

@app.get("/sites/{site_id}/energy")
def get_site_energy(site_id: str):

    query = text("""
        SELECT
            date,
            hour,
            hourly_energy_consumption
        FROM fact_energy
        ORDER BY date DESC, hour DESC
        LIMIT 24
    """)

    with engine.connect() as conn:
        result = conn.execute(query)

        rows = [
            dict(row._mapping)
            for row in result
        ]

    return rows

@app.get("/assets/{asset_id}/health")
def get_asset_health(asset_id: str):

    query = text("""
        SELECT *
        FROM fact_asset_health
        WHERE asset_id = :asset_id
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"asset_id": asset_id})

        row = result.fetchone()

    if row:
        return dict(row._mapping)

    return {"message": "Asset not found"}

@app.get("/sites/{site_id}/assets")
def get_site_assets(site_id: str):

    query = text("""
        SELECT
            asset_id,
            asset_name,
            asset_type,
            category,
            manufacturer
        FROM dim_asset
        WHERE site_id = :site_id
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"site_id": site_id})

        rows = [
            dict(row._mapping)
            for row in result
        ]

    return rows