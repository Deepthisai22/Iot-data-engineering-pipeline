import pandas as pd
from sqlalchemy import create_engine
import logging
import os

from urllib.parse import quote_plus

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "nectar_iot_dw"
DB_USER = "postgres"
DB_PASSWORD = "Postgres@123"

# =====================================================
# Create PostgreSQL Connection
# =====================================================

def create_database_connection():

    print("\nConnecting to PostgreSQL...")

    logging.info("Connecting to PostgreSQL.")

    encoded_password = quote_plus(DB_PASSWORD)

    engine = create_engine(
    
        f"postgresql://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    print("Connected successfully.")

    logging.info("Connected successfully.")

    return engine

def load_csv_to_table(engine, csv_path, table_name):
    """
    Load CSV file into PostgreSQL table.
    """

    try:
        df = pd.read_csv(csv_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

        print(f"✅ {table_name} loaded successfully.")
        logging.info(f"{table_name} loaded successfully.")

    except Exception as e:
        print(f"❌ Error loading {table_name}: {e}")
        logging.error(f"Error loading {table_name}: {e}")

# =====================================================
# Load Dimension Tables
# =====================================================

def load_dimension_tables(engine):

    print("\nLoading Dimension Tables...")
    logging.info("Loading Dimension Tables.")

    load_csv_to_table(
        engine,
        "data/raw/sites.csv",
        "dim_site"
    )

    load_csv_to_table(
        engine,
        "data/raw/buildings.csv",
        "dim_building"
    )

    load_csv_to_table(
        engine,
        "data/raw/assets.csv",
        "dim_asset"
    )

    load_csv_to_table(
        engine,
        "data/raw/dim_time.csv",
        "dim_time"
    )

    print("Dimension Tables Loaded Successfully.\n")

def load_fact_tables(engine):

    print("\nLoading Fact Tables...")
    logging.info("Loading Fact Tables.")

    load_csv_to_table(
        engine,
        "data/raw/iot_telemetry.csv",
        "fact_telemetry"
    )

    load_csv_to_table(
        engine,
        "data/raw/event_data.csv",
        "fact_event"
    )
    
    load_csv_to_table(
    engine,
    "data/processed/hourly_energy_consumption.csv",
    "fact_energy"
    )

    load_csv_to_table(
        engine,
        "data/processed/asset_risk_level.csv",
        "fact_asset_health"
    )

    #load_csv_to_table(
    #  engine,
    #  "data/processed/maintenance_recommendations.csv",
    #  "fact_maintenance"
    #)

    print("Fact Tables Loaded Successfully.\n")

# =====================================================
# Main Function
# =====================================================

def main():

    engine = create_database_connection()

    print("\nDatabase connection established.")
    logging.info("Database connection established.")

    load_dimension_tables(engine)

    load_fact_tables(engine)

    print("\nAll tables loaded successfully!")


if __name__ == "__main__":
    main()