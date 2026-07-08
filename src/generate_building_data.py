import pandas as pd
import random
import os

# =====================================================
# File Paths
# =====================================================

RAW_DATA_PATH = "data/raw"

SITES_FILE = os.path.join(RAW_DATA_PATH, "sites.csv")
BUILDINGS_FILE = os.path.join(RAW_DATA_PATH, "buildings.csv")

# =====================================================
# Building Names
# =====================================================

BUILDING_NAMES = [
    "Main Building",
    "Administration Block",
    "Emergency Block",
    "ICU Block",
    "Outpatient Block",
    "Research Center",
    "Diagnostics Center",
    "Warehouse",
    "Utility Block",
    "Operations Center"
]

# =====================================================
# Generate Buildings
# =====================================================

def generate_buildings():

    print("Reading Sites...")

    sites_df = pd.read_csv(SITES_FILE)

    building_records = []

    building_counter = 1

    random.seed(42)

    for _, site in sites_df.iterrows():

        number_of_buildings = random.randint(2, 5)

        selected_names = random.sample(
            BUILDING_NAMES,
            number_of_buildings
        )

        for building_name in selected_names:

            building_records.append({

                "building_id": f"BLD{building_counter:04d}",

                "site_id": site["site_id"],

                "building_name": building_name

            })

            building_counter += 1

    building_df = pd.DataFrame(building_records)

    building_df.to_csv(
        BUILDINGS_FILE,
        index=False
    )

    print("\nBuildings Generated Successfully!")

    print(f"Total Buildings : {len(building_df)}")

    print(f"Saved to : {BUILDINGS_FILE}")


# =====================================================
# Main Function
# =====================================================

def main():

    generate_buildings()


if __name__ == "__main__":
    main()