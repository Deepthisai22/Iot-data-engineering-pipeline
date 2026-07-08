import pandas as pd

# Read telemetry dataset
telemetry_df = pd.read_csv("data/raw/iot_telemetry.csv")

# Convert timestamp to datetime
telemetry_df["timestamp"] = pd.to_datetime(telemetry_df["timestamp"])

# Get unique timestamps
time_df = pd.DataFrame({
    "full_date": telemetry_df["timestamp"].drop_duplicates()
}).sort_values("full_date")

# Create surrogate key
time_df.insert(
    0,
    "time_id",
    ["TIME{:06d}".format(i) for i in range(1, len(time_df) + 1)]
)

# Extract date parts
time_df["hour"] = time_df["full_date"].dt.hour
time_df["day"] = time_df["full_date"].dt.day
time_df["month"] = time_df["full_date"].dt.month
time_df["quarter"] = time_df["full_date"].dt.quarter
time_df["year"] = time_df["full_date"].dt.year
time_df["weekday"] = time_df["full_date"].dt.day_name()

# Save CSV
time_df.to_csv("data/raw/dim_time.csv", index=False)

print("=" * 60)
print("Time Dimension Generated")
print("=" * 60)
print(time_df.head())
print(f"\nTotal Time Records : {len(time_df)}")
print("\ndim_time.csv saved successfully!")