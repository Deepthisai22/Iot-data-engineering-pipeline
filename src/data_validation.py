import os
import logging

import pandas as pd

from datetime import datetime, timedelta

import json

logging.basicConfig(
    filename="logs/data_validation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

RAW_DATA_PATH = "data/raw"
VALIDATED_DATA_PATH = "data/validated"

SITE_COLUMNS = [
    "site_id",
    "customer_id",
    "customer_name",
    "industry",
    "city",
    "site_type",
    "site_name"
]

ASSET_METADATA_COLUMNS = [
    "asset_id",
    "asset_type",
    "asset_name",
    "category",
    "manufacturer",
    "installation_date",
    "warranty_expiry",
    "site_id",
    "building_id",
    "customer_id",
    "industry",
    "city",
    "site_type",
    "site_name"
]

TELEMETRY_COLUMNS = [
    "timestamp",
    "site_id",
    "building_id",
    "asset_id",
    "sensor_id",
    "temperature",
    "humidity",
    "pressure",
    "vibration",
    "power_consumption",
    "operating_mode"
]

EVENT_COLUMNS = [
    "event_id",
    "timestamp",
    "asset_id",
    "event_type",
    "severity",
    "message"
]

def load_csv(file_name):

    file_path = os.path.join(RAW_DATA_PATH, file_name)

    if not os.path.exists(file_path):
        logging.error(f"{file_name} not found.")
        raise FileNotFoundError(f"{file_name} not found.")

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
def check_missing_values(df, dataset_name):

    print(f"\nChecking missing values in {dataset_name}...")

    missing = df.isnull().sum()

    print(missing)

    logging.info(f"Missing value check completed for {dataset_name}")

    return missing

def check_duplicates(df, dataset_name):

    print(f"\nChecking duplicate records in {dataset_name}...")

    duplicate_count = df.duplicated().sum()

    print(f"Duplicate Records : {duplicate_count}")

    logging.info(
        f"Duplicate check completed for {dataset_name}. "
        f"Duplicates found: {duplicate_count}"
    )

    return duplicate_count

def validate_columns(df, expected_columns, dataset_name):

    print(f"\nValidating columns in {dataset_name}...")

    actual_columns = list(df.columns)

    if actual_columns == expected_columns:
        print("Column validation passed.")
        logging.info(f"{dataset_name}: Column validation passed.")
        return True

    else:
        print("Column validation failed.")

        print(f"Expected: {expected_columns}")
        print(f"Actual  : {actual_columns}")

        logging.error(f"{dataset_name}: Column validation failed.")

        return False

def validate_timestamp(df, column_name, dataset_name):

    print(f"\nValidating timestamps in {dataset_name}...")

    validation_passed = True

    try:
        pd.to_datetime(df[column_name], errors="raise")

        print("Timestamp validation passed.")
        logging.info(f"{dataset_name}: Timestamp validation passed.")

    except Exception:

        print("Invalid timestamps found.")
        logging.error(f"{dataset_name}: Invalid timestamps found.")

        validation_passed = False

    return validation_passed

def validate_asset_ids(df, asset_metadata_df, dataset_name):

    print(f"\nValidating Asset IDs in {dataset_name}...")

    validation_passed = True

    valid_asset_ids = set(asset_metadata_df["asset_id"])

    invalid_asset_ids = df.loc[
        ~df["asset_id"].isin(valid_asset_ids),
        "asset_id"
    ].unique()

    if len(invalid_asset_ids) == 0:

        print("Asset ID validation passed.")
        logging.info(f"{dataset_name}: Asset ID validation passed.")

    else:

        print("Invalid Asset IDs found:")
        print(invalid_asset_ids)

        logging.error(f"{dataset_name}: Invalid Asset IDs found.")

        validation_passed = False

    return validation_passed

def validate_sites(sites_df):

    print("\nValidating Sites Business Rules...")

    validation_passed = True

    if not sites_df["site_id"].str.startswith("SITE").all():

        print("Invalid Site IDs found.")
        logging.error("Invalid Site IDs found.")

        validation_passed = False

    if not sites_df["customer_id"].str.startswith("CUST").all():

        print("Invalid Customer IDs found.")
        logging.error("Invalid Customer IDs found.")

        validation_passed = False

    if validation_passed:

        print("Sites business validation passed.")
        logging.info("Sites business validation passed.")

    return validation_passed

def validate_datatypes(df, expected_dtypes, dataset_name):

    print(f"\nValidating datatypes in {dataset_name}...")

    validation_passed = True

    for column, expected_dtype in expected_dtypes.items():

        actual_dtype = str(df[column].dtype)

        if actual_dtype != expected_dtype:

            print(
                f"{column}: Expected {expected_dtype}, "
                f"Found {actual_dtype}"
            )

            logging.error(
                f"{dataset_name}: {column} datatype mismatch."
            )

            validation_passed = False

    if validation_passed:
        print("Datatype validation passed.")
        logging.info(f"{dataset_name}: Datatype validation passed.")

    return validation_passed


# =====================================================
# Validate Primary Key
# =====================================================

def validate_primary_key(df, primary_key, dataset_name):

    print(f"\nValidating primary key in {dataset_name}...")

    duplicate_keys = df[primary_key].duplicated().sum()

    if duplicate_keys == 0:

        print(f"{primary_key} is unique.")

        logging.info(
            f"{dataset_name}: Primary key validation passed."
        )

        return True

    else:

        print(
            f"{duplicate_keys} duplicate "
            f"{primary_key} values found."
        )

        logging.error(
            f"{dataset_name}: Duplicate primary keys found."
        )

        return False

# =====================================================
# Validate Foreign Key
# =====================================================

def validate_foreign_key(
    child_df,
    parent_df,
    foreign_key,
    dataset_name
):

    print(f"\nValidating foreign key in {dataset_name}...")

    invalid_records = (
        ~child_df[foreign_key]
        .isin(parent_df[foreign_key])
    ).sum()

    if invalid_records == 0:

        print("Foreign key validation passed.")

        logging.info(
            f"{dataset_name}: Foreign key validation passed."
        )

        return True

    else:

        print(
            f"{invalid_records} invalid "
            f"{foreign_key} values found."
        )

        logging.error(
            f"{dataset_name}: Foreign key validation failed."
        )

        return False
# =====================================================
# Validate Telemetry Business Rules
# =====================================================

def validate_telemetry(telemetry_df):

    print("\nValidating Telemetry Business Rules...")

    validation_passed = True

    valid_modes = [
        "Running",
        "Idle",
        "Maintenance",
        "Shutdown"
    ]

    if not telemetry_df["temperature"].between(0, 100).all():

        print("Invalid temperature values found.")

        validation_passed = False

    if not telemetry_df["humidity"].between(0, 100).all():

        print("Invalid humidity values found.")

        validation_passed = False

    if (telemetry_df["pressure"] <= 0).any():

        print("Invalid pressure values found.")

        validation_passed = False

    if (telemetry_df["vibration"] < 0).any():

        print("Invalid vibration values found.")

        validation_passed = False

    if (telemetry_df["power_consumption"] < 0).any():

        print("Invalid power consumption values found.")

        validation_passed = False

    if not telemetry_df["operating_mode"].isin(valid_modes).all():

        print("Invalid operating mode found.")

        validation_passed = False

    if validation_passed:

        print("Telemetry business validation passed.")

        logging.info("Telemetry business validation passed.")

    else:

        logging.error("Telemetry business validation failed.")

    return validation_passed

# =====================================================
# Validate Sites Business Rules
# =====================================================

def validate_sites(sites_df):

    print("\nValidating Sites Business Rules...")

    validation_passed = True

    valid_industries = [
        "Healthcare",
        "Retail",
        "Commercial Offices",
        "Manufacturing",
        "Hospitality"
    ]

    if not sites_df["industry"].isin(valid_industries).all():

        print("Invalid industry values found.")

        validation_passed = False

    if sites_df["city"].isnull().any():

        print("Missing city values found.")

        validation_passed = False

    if sites_df["site_name"].isnull().any():

        print("Missing site name values found.")

        validation_passed = False

    if validation_passed:

        print("Sites business validation passed.")

        logging.info("Sites business validation passed.")

    else:

        logging.error("Sites business validation failed.")

    return validation_passed

def validate_asset_metadata(asset_metadata_df):

    print("\nValidating Asset Metadata Business Rules...")

    validation_passed = True

    installation_dates = pd.to_datetime(asset_metadata_df["installation_date"])
    warranty_dates = pd.to_datetime(asset_metadata_df["warranty_expiry"])

    if not (installation_dates < warranty_dates).all():

        print("Invalid installation/warranty dates found.")
        logging.error("Invalid installation/warranty dates found.")

        validation_passed = False

    valid_asset_types = [
        "MRI Scanner",
        "CT Scanner",
        "X-Ray Machine",
        "Ventilator",
        "Defibrillator",
        "Ultrasound Machine",
        "Patient Monitor"
    ]

    if not asset_metadata_df["asset_type"].isin(valid_asset_types).all():

        print("Invalid asset types found.")
        logging.error("Invalid asset types found.")

        validation_passed = False

    valid_categories = [
        "Imaging",
        "Critical Care",
        "Monitoring"
    ]

    if not asset_metadata_df["category"].isin(valid_categories).all():

        print("Invalid categories found.")
        logging.error("Invalid categories found.")

        validation_passed = False

    if validation_passed:

        print("Asset Metadata business validation passed.")
        logging.info("Asset Metadata business validation passed.")

    return validation_passed

# =====================================================
# Validate Asset Metadata Business Rules
# =====================================================

def validate_asset_metadata(asset_metadata_df):

    print("\nValidating Asset Metadata Business Rules...")

    validation_passed = True

    installation = pd.to_datetime(
        asset_metadata_df["installation_date"]
    )

    warranty = pd.to_datetime(
        asset_metadata_df["warranty_expiry"]
    )

    if (installation >= warranty).any():

        print("Invalid installation/warranty dates found.")

        validation_passed = False

    if validation_passed:

        print("Asset Metadata business validation passed.")

        logging.info(
            "Asset Metadata business validation passed."
        )

    else:

        logging.error(
            "Asset Metadata business validation failed."
        )

    return validation_passed

def validate_telemetry(telemetry_df):

    print("\nValidating Telemetry Business Rules...")

    validation_passed = True

    valid_modes = [
       "Running",
       "Idle",
       "Maintenance",
       "Shutdown"
    ]

    if not telemetry_df["temperature"].between(-20, 80).all():

       print("Invalid temperature values found.")
       logging.error("Invalid temperature values found.")

       validation_passed = False

    if not telemetry_df["humidity"].between(0, 100).all():

       print("Invalid humidity values found.")
       logging.error("Invalid humidity values found.")

       validation_passed = False

    if not telemetry_df["pressure"].between(800, 1200).all():

       print("Invalid pressure values found.")
       logging.error("Invalid pressure values found.")

       validation_passed = False

    if (telemetry_df["vibration"] < 0).any():

       print("Invalid vibration values found.")
       logging.error("Invalid vibration values found.")

       validation_passed = False
    
    if (telemetry_df["power_consumption"] < 0).any():

       print("Invalid power consumption values found.")
       logging.error("Invalid power consumption values found.")

       validation_passed = False


    if not telemetry_df["operating_mode"].isin(valid_modes).all():

       print("Invalid operating mode values found.")
       logging.error("Invalid operating mode values found.")

       validation_passed = False

    if validation_passed:

       print("Telemetry business validation passed.")
       logging.info("Telemetry business validation passed.")

    else:

       logging.error("Telemetry business validation failed.")

    return validation_passed

# =====================================================
# Validate Event Business Rules
# =====================================================

def validate_events(events_df):

    print("\nValidating Event Business Rules...")

    validation_passed = True

    valid_severity = [
        "Low",
        "Medium",
        "High"
    ]

    valid_event_types = [
        "Alarm",
        "Warning",
        "Fault",
        "Maintenance"
    ]

    if not events_df["severity"].isin(valid_severity).all():

        print("Invalid severity values found.")

        validation_passed = False

    if not events_df["event_type"].isin(valid_event_types).all():

        print("Invalid event type values found.")

        validation_passed = False

    if events_df["message"].str.strip().eq("").any():

        print("Empty event messages found.")

        logging.error("Empty event messages found.")

        validation_passed = False

    if validation_passed:

        print("Event business validation passed.")

        logging.info("Event business validation passed.")

    else:

        logging.error("Event business validation failed.")

    return validation_passed


# =====================================================
# Detect Outliers
# =====================================================

def detect_outliers(df, column_name):

    print(f"\nChecking outliers in {column_name}...")

    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - (1.5 * IQR)
    upper_limit = Q3 + (1.5 * IQR)

    outliers = df[
        (df[column_name] < lower_limit)
        |
        (df[column_name] > upper_limit)
    ]

    print(f"Outliers found: {len(outliers)}")

    logging.info(
        f"{column_name}: {len(outliers)} outliers found."
    )

    return outliers

# =====================================================
# Detect Late Arriving Data
# =====================================================

def detect_late_arriving_data(df):

    print("\nChecking late arriving telemetry data...")

    # Dataset does not contain an arrival timestamp,
    # so true late-arriving records cannot be determined.
    late_records = pd.DataFrame(columns=df.columns)

    print(f"Late records found: {len(late_records)}")

    logging.info(
        f"Late arriving records: {len(late_records)}"
    )

    return late_records

# =====================================================
# Generate Data Quality Report
# =====================================================

def generate_data_quality_report(
    telemetry_outliers,
    temperature_outliers,
    late_records
):

    report = {
        "Power Consumption Outliers": len(telemetry_outliers),
        "Temperature Outliers": len(temperature_outliers),
        "Late Arriving Records": len(late_records),
        "Report Generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("logs/data_quality_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nData Quality Report Generated Successfully.")
# =====================================================
# Save Validated Data
# =====================================================

def save_validated_data(df, file_name):

    os.makedirs(VALIDATED_DATA_PATH, exist_ok=True)

    output_path = os.path.join(
        VALIDATED_DATA_PATH,
        file_name
    )

    df.to_csv(output_path, index=False)

    print(f"{file_name} saved successfully.")

    logging.info(f"{file_name} saved to validated folder.")

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

        # Missing Values
    check_missing_values(sites_df, "Sites")
    check_missing_values(asset_metadata_df, "Asset Metadata")
    check_missing_values(telemetry_df, "Telemetry")
    check_missing_values(events_df, "Events")

    # Duplicate Records
    check_duplicates(sites_df, "Sites")
    check_duplicates(asset_metadata_df, "Asset Metadata")
    check_duplicates(telemetry_df, "Telemetry")
    check_duplicates(events_df, "Events")

    # Column Validation
    validate_columns(
      sites_df,
      SITE_COLUMNS,
      "Sites"
    )

    validate_columns(
      asset_metadata_df,
      ASSET_METADATA_COLUMNS,
      "Asset Metadata"
    )

    validate_columns(
      telemetry_df,
      TELEMETRY_COLUMNS,
      "Telemetry"
    )

    validate_columns(
      events_df,
      EVENT_COLUMNS,
      "Events"
    )

    # Timestamp Validation

    validate_timestamp(
      telemetry_df,
      "timestamp",
      "Telemetry"
    )

    validate_timestamp(
      events_df,
      "timestamp",
      "Events"
    )

    # Asset ID Validation

    validate_asset_ids(
      telemetry_df,
      asset_metadata_df,
      "Telemetry"
    )

    validate_asset_ids(
      events_df,
      asset_metadata_df,
      "Events"
    )

    # Sites Business Validation

    validate_sites(sites_df)

    validate_asset_metadata(asset_metadata_df)

    validate_telemetry(telemetry_df)

    validate_events(events_df)

    save_validated_data(
       sites_df,
       "sites.csv"
    )

    save_validated_data(
        asset_metadata_df,
        "asset_metadata.csv"
    )

    save_validated_data(
        telemetry_df,
        "iot_telemetry.csv"
    )

    save_validated_data(
        events_df,
       "event_data.csv"
    )
    power_outliers = detect_outliers(
    telemetry_df,
    "power_consumption"
    )

    temperature_outliers = detect_outliers(
       telemetry_df,
         "temperature"
    )

    late_records = detect_late_arriving_data(
       telemetry_df
    )

    generate_data_quality_report(
       power_outliers,
        temperature_outliers,
        late_records
    )

if __name__ == "__main__": 
    main()
 