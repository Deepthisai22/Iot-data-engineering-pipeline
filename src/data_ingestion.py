import os
import logging

import pandas as pd

logging.basicConfig(
    filename="logs/data_ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
RAW_DATA_PATH = "data/raw"

def load_csv(file_name):

    file_path = os.path.join(
        RAW_DATA_PATH,
        file_name
    )

    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")

        raise FileNotFoundError(
        f"File not found: {file_path}"
        )
    df = pd.read_csv(file_path)

    logging.info(f"{file_name} loaded successfully.") 

    return df

def load_all_data():

    sites_df = load_csv("sites.csv")

    asset_metadata_df = load_csv("asset_metadata.csv")

    telemetry_df = load_csv("iot_telemetry.csv")

    events_df = load_csv("event_data.csv")

    return (
        sites_df,
        asset_metadata_df,
        telemetry_df,
        events_df
    )
# =====================================================
# Main Function
# =====================================================

def main():

    (
        sites_df,
        asset_metadata_df,
        telemetry_df,
        events_df
    ) = load_all_data()

    print("=" * 60)
    print("DATA INGESTION COMPLETED")
    print("=" * 60)

    print(f"Sites Dataset Loaded            : {len(sites_df)} records")
    print(f"Asset Metadata Dataset Loaded   : {len(asset_metadata_df)} records")
    print(f"IoT Telemetry Dataset Loaded    : {len(telemetry_df)} records")
    print(f"Event Dataset Loaded            : {len(events_df)} records")

    print("\nSites preview:")
    print(sites_df.head())
    print(sites_df.shape)

    logging.info("All datasets loaded successfully.")


if __name__ == "__main__":
    main()