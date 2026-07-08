import os
import logging

import pandas as pd

logging.basicConfig(
    filename="logs/data_transformation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

VALIDATED_DATA_PATH = "data/validated"
PROCESSED_DATA_PATH = "data/processed"

# =====================================================
# Load CSV File
# =====================================================

def load_csv(file_name):

    file_path = os.path.join(
        VALIDATED_DATA_PATH,
        file_name
    )

    if not os.path.exists(file_path):

        logging.error(f"{file_name} not found.")

        raise FileNotFoundError(
            f"{file_name} not found."
        )

    df = pd.read_csv(file_path)

    logging.info(f"{file_name} loaded successfully.")

    return df

# =====================================================
# Load All Validated Datasets
# =====================================================

def load_all_data():

    sites_df = load_csv("sites.csv")

    asset_metadata_df = load_csv(
        "asset_metadata.csv"
    )

    telemetry_df = load_csv(
        "iot_telemetry.csv"
    )

    events_df = load_csv(
        "event_data.csv"
    )

    return (
        sites_df,
        asset_metadata_df,
        telemetry_df,
        events_df
    )

# =====================================================
# Prepare Telemetry Data
# =====================================================

def prepare_telemetry_data(telemetry_df):
    print("\nPreparing Telemetry Data...")

    logging.info("Preparing telemetry data.")

    telemetry_df["timestamp"] = pd.to_datetime(
        telemetry_df["timestamp"]
    )

    telemetry_df["date"] = (
        telemetry_df["timestamp"]
        .dt.date
    )

    telemetry_df["hour"] = (
        telemetry_df["timestamp"]
        .dt.hour
    )

    telemetry_df["day_of_week"] = (
        telemetry_df["timestamp"]
        .dt.day_name()
    )

    telemetry_df = telemetry_df.sort_values(
    by=[
        "asset_id",
        "timestamp"
       ]
    )

    print("Telemetry data prepared successfully.")

    logging.info(
        "Telemetry data prepared successfully."
    )

    return telemetry_df

# =====================================================
# Hourly Energy Consumption
# =====================================================

def create_hourly_energy_consumption(telemetry_df):
    print("\nCreating Hourly Energy Consumption...")

    logging.info(
       "Creating Hourly Energy Consumption."
    )

    hourly_energy = (
        telemetry_df
        .groupby(
            ["date", "hour"]
        )["power_consumption"]
        .sum()
        .reset_index()
    )

    hourly_energy.rename(
        columns={
           "power_consumption":
           "hourly_energy_consumption"
        },
        inplace=True
    )

    print(
        "Hourly Energy Consumption created successfully."
    )

    logging.info(
        "Hourly Energy Consumption created successfully."
    )

    return hourly_energy

# =====================================================
# Daily Asset Utilization
# =====================================================

def create_daily_asset_utilization(telemetry_df):

    print("\nCreating Daily Asset Utilization...")

    logging.info(
        "Creating Daily Asset Utilization."
    )
    total_readings = (

       telemetry_df

       .groupby(
           ["date", "asset_id"]
        )

        .size()

        .reset_index(name="total_readings")

    )

    running_readings = (

        telemetry_df[
            telemetry_df["operating_mode"] == "Running"
        ]

        .groupby(
            ["date", "asset_id"]
        )

        .size()

        .reset_index(name="running_readings")

    )

    daily_utilization = total_readings.merge(

        running_readings,

        on=[
           "date",
           "asset_id"
        ],

        how="left"

    )

    daily_utilization[
        "running_readings"
    ] = daily_utilization[
        "running_readings"
    ].fillna(0)

    daily_utilization[
        "utilization_percentage"
    ] = (

        daily_utilization[
            "running_readings"
        ]

        /

        daily_utilization[
            "total_readings"
        ]
    ) * 100

    daily_utilization[
        "utilization_percentage"
    ] = daily_utilization[
        "utilization_percentage"
    ].round(2)

    print(
       "Daily Asset Utilization created successfully."
    )

    logging.info(
        "Daily Asset Utilization created successfully."
    )

    return daily_utilization

# =====================================================
# Average Environmental Conditions
# =====================================================

def create_average_environmental_conditions(
    telemetry_df
):

    print("\nCreating Average Environmental Conditions...")

    logging.info(
        "Creating Average Environmental Conditions."
    )

    average_environment = (

       telemetry_df

       .groupby(
          "date"
        )

       .agg(

            average_temperature=(
                "temperature",
                "mean"
            ),

            average_humidity=(
                "humidity",
                "mean"
            ),

            average_pressure=(
                "pressure",
                "mean"
            ),

            average_vibration=(
                "vibration",
                "mean"
            )

        )

        .reset_index()

    )

    average_environment = average_environment.round(2)

    print(
        "Average Environmental Conditions created successfully."
    )

    logging.info(
        "Average Environmental Conditions created successfully."
    )

    return average_environment

# =====================================================
# Fault Statistics Per Asset
# =====================================================

def create_fault_statistics(events_df):

    print("\nCreating Fault Statistics Per Asset...")

    logging.info(
        "Creating Fault Statistics Per Asset."
    )

    fault_events = events_df[
        events_df["event_type"] == "Fault"
    ]

    fault_statistics = (
        fault_events
        .groupby(
            "asset_id"
        )
        .size()
        .reset_index(
            name="fault_count"
        )
    )

    fault_statistics = fault_statistics.sort_values(
        by="fault_count",
        ascending=False
    )

    print(
        "Fault Statistics created successfully."
    )

    logging.info(
        "Fault Statistics created successfully."
    )

    return fault_statistics

def save_transformed_data(df, file_name):

    os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

    output_path = os.path.join(PROCESSED_DATA_PATH, file_name)

    df.to_csv(output_path, index=False)

    print(f"{file_name} saved successfully.")

    logging.info(f"{file_name} saved successfully.")

# =========================================
# Data Aggregation Functions
# =========================================

def create_site_metrics(
    telemetry_df,
    events_df,
    asset_metadata_df
):

    print("\nCreating Site-Level Metrics...")

    logging.info("Creating Site-Level Metrics.")

    telemetry_site = telemetry_df

    events_site = events_df.merge(
    asset_metadata_df[["asset_id", "site_id"]],
    on="asset_id",
    how="left"
)


    site_faults = (
        events_site[
           events_site["event_type"] == "Fault"
        ]
            .groupby("site_id")
            .size()
            .reset_index(name="total_faults")
    )


    site_metrics = (
        telemetry_site
        .groupby("site_id")
        .agg(
            total_energy=("power_consumption", "sum"),
            average_temperature=("temperature", "mean"),
            average_humidity=("humidity", "mean")
        )
        .reset_index()
    )
    site_metrics = site_metrics.merge(
       site_faults,
       on="site_id",
       how="left"
    )

    site_metrics["total_faults"] = (
       site_metrics["total_faults"]
        .fillna(0)
        .astype(int)
    )
    return site_metrics


# =====================================================
# Building-Level Metrics
# =====================================================

def create_building_metrics(
    telemetry_df,
    events_df,
    asset_metadata_df
):

    print("\nCreating Building-Level Metrics...")

    logging.info("Creating Building-Level Metrics.")

    telemetry_building = telemetry_df

    events_building = events_df.merge(
    asset_metadata_df[["asset_id", "building_id"]],
    on="asset_id",
    how="left"
)


    building_faults = (
        events_building[
            events_building["event_type"] == "Fault"
        ]
        .groupby("building_id")
        .size()
        .reset_index(name="total_faults")
    )

    building_metrics = (
        telemetry_building
        .groupby("building_id")
        .agg(
            total_energy=("power_consumption", "sum"),
            average_temperature=("temperature", "mean"),
            average_humidity=("humidity", "mean")
        )
        .reset_index()
    )

    building_metrics = building_metrics.merge(
        building_faults,
        on="building_id",
        how="left"
    )

    building_metrics["total_faults"] = (
        building_metrics["total_faults"]
        .fillna(0)
        .astype(int)
    )

    return building_metrics


# =====================================================
# Asset-Level Metrics
# =====================================================

def create_asset_metrics(
    telemetry_df,
    events_df
):

    print("\nCreating Asset-Level Metrics...")

    logging.info("Creating Asset-Level Metrics.")

    asset_faults = (
        events_df[
            events_df["event_type"] == "Fault"
        ]
        .groupby("asset_id")
        .size()
        .reset_index(name="total_faults")
    )

    asset_metrics = (
        telemetry_df
        .groupby("asset_id")
        .agg(
            total_energy=("power_consumption", "sum"),
            average_power=("power_consumption", "mean"),
            average_temperature=("temperature", "mean"),
            average_humidity=("humidity", "mean"),
            average_pressure=("pressure", "mean"),
            average_vibration=("vibration", "mean")
        )
        .reset_index()
    )

    asset_metrics = asset_metrics.merge(
    asset_faults,
    on="asset_id",
    how="left"
    )

    asset_metrics["total_faults"] = (
    asset_metrics["total_faults"]
    .fillna(0)
    .astype(int)
    )

    telemetry_asset = telemetry_df
    events_asset = events_df

    return asset_metrics

def create_asset_health_score(asset_metrics_df):

    print("\nCreating Asset Health Score...")

    logging.info("Creating Asset Health Score.")

    health_df = asset_metrics_df.copy()
    health_df["health_score"] = (
    100
    - (health_df["total_faults"] * 2)
    - (health_df["average_vibration"] * 5)
    - (health_df["average_temperature"] - 25)
    )

    health_df["health_score"] = (
    health_df["health_score"]
    .clip(lower=0, upper=100)
    .round(2)
    )

    return health_df

# =====================================================
# Asset Risk Level
# =====================================================

def create_asset_risk_level(asset_health_df):

    print("\nCreating Asset Risk Level...")

    logging.info("Creating Asset Risk Level.")

    risk_df = asset_health_df.copy()

    risk_df["risk_level"] = "Low"

    risk_df.loc[
        risk_df["health_score"] < 80,
        "risk_level"
    ] = "Medium"

    risk_df.loc[
        risk_df["health_score"] < 60,
        "risk_level"
    ] = "High"

    print("Asset Risk Level created successfully.")

    return risk_df


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

    telemetry_df = prepare_telemetry_data(telemetry_df)

    hourly_energy_df = create_hourly_energy_consumption(telemetry_df)

    daily_asset_utilization_df = create_daily_asset_utilization(telemetry_df)

    average_environment_df = create_average_environmental_conditions(telemetry_df)

    fault_statistics_df = create_fault_statistics(events_df)

    # =====================================
    # Data Aggregation
    # =====================================

    site_metrics_df = create_site_metrics(
        telemetry_df,
        events_df,
        asset_metadata_df
    )

    building_metrics_df = create_building_metrics(
        telemetry_df,
        events_df,
        asset_metadata_df
    )

    asset_metrics_df = create_asset_metrics(
        telemetry_df,
        events_df
    )
    asset_health_df = create_asset_health_score(
    asset_metrics_df
    )

    asset_risk_df = create_asset_risk_level(
    asset_health_df
)

    # =====================================
    # Saved Processed Data
    # =====================================


    save_transformed_data(
        hourly_energy_df,
        "hourly_energy_consumption.csv"
    )

    save_transformed_data(
        daily_asset_utilization_df,
        "daily_asset_utilization.csv"
    )

    save_transformed_data(
        average_environment_df,
        "average_environmental_conditions.csv"
    )

    save_transformed_data(
        fault_statistics_df,
        "fault_statistics.csv"
    )

    save_transformed_data(
        site_metrics_df,
        "site_metrics.csv"
    )

    save_transformed_data(
        building_metrics_df,
        "building_metrics.csv"
    )

    save_transformed_data(
        asset_metrics_df,
       "asset_metrics.csv"
    )
    
    save_transformed_data(
        asset_health_df,
        "asset_health_score.csv"
    )

    save_transformed_data(
        asset_risk_df,
        "asset_risk_level.csv"
    )

if __name__ == "__main__":
    main()