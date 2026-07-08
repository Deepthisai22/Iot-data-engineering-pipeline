import random
import pandas as pd
from datetime import datetime, timedelta

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

random.seed(42)

customers = [
    {
        "customer_id": "CUST001",
        "customer_name": "MedCare Health Network",
        "industry": "Healthcare",

        "min_sites": 5,
        "max_sites": 10
    },
    {
        "customer_id": "CUST002",
        "customer_name": "UrbanSquare Retail Group",
        "industry": "Retail",

        "min_sites": 3,
        "max_sites": 8
    },
    {
        "customer_id": "CUST003",
        "customer_name": "NovaTech Business Parks",
        "industry": "Commercial Offices",

        "min_sites": 4,
        "max_sites": 10
    },
    {
        "customer_id": "CUST004",
        "customer_name": "AquaPure Manufacturing",
        "industry": "Manufacturing",

        "min_sites": 3,
        "max_sites": 7
    },
    {
        "customer_id": "CUST005",
        "customer_name": "SkyStay Hotels & Resorts",
        "industry": "Hospitality",

        "min_sites": 6,
        "max_sites": 12
    }


]

healthcare_cities = [
    "Hyderabad",
    "Warangal",
    "Vijayawada",
    "Visakhapatnam",
    "Tirupati",
    "Kurnool",
    "Nellore",
    "Rajahmundry"
]

healthcare_site_types = [
    "Central Hospital",
    "Medical Center",
    "Specialty Hospital",
    "Children's Hospital",
    "Multi-Speciality Hospital"
]

retail_cities = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Pune",
    "Kochi",
    "Coimbatore"
]

retail_site_types = [
    "City Mall",
    "Shopping Plaza",
    "Retail Hub",
    "Lifestyle Center"
]

office_cities = [
    "Hyderabad",
    "Bengaluru",
    "Pune",
    "Chennai",
    "Noida",
    "Gurugram"
]

office_site_types = [
    "Tech Park",
    "Business Park",
    "Corporate Campus",
    "Innovation Center"
]

manufacturing_cities = [
    "Hyderabad",
    "Visakhapatnam",
    "Chennai",
    "Pune",
    "Ahmedabad",
    "Surat"
]

manufacturing_site_types = [
    "Manufacturing Plant",
    "Production Facility",
    "Industrial Unit",
    "Processing Plant"
]

hospitality_cities = [
    "Goa",
    "Hyderabad",
    "Jaipur",
    "Udaipur",
    "Mysuru",
    "Kochi",
    "Ooty"
]

hospitality_site_types = [
    "Grand Hotel",
    "Resort",
    "Luxury Suites",
    "Business Hotel"
]



def generate_site_pool(city_list, site_type_list):

    site_pool = []

    for city in city_list:

        for site_type in site_type_list:

            site_name = f"{city} {site_type}"

            site_pool.append({
                "city": city,
                "site_type": site_type,
                "site_name": site_name
            })

    return site_pool

healthcare_site_pool = generate_site_pool(
    healthcare_cities,
    healthcare_site_types
)

retail_site_pool = generate_site_pool(
    retail_cities,
    retail_site_types
)

office_site_pool = generate_site_pool(
    office_cities,
    office_site_types
)

manufacturing_site_pool = generate_site_pool(
    manufacturing_cities,
    manufacturing_site_types
)

hospitality_site_pool = generate_site_pool(
    hospitality_cities,
    hospitality_site_types
)

random.shuffle(healthcare_site_pool)
random.shuffle(retail_site_pool)
random.shuffle(office_site_pool)
random.shuffle(manufacturing_site_pool)
random.shuffle(hospitality_site_pool)

# =====================================================
# Healthcare Asset Configuration
# =====================================================

healthcare_assets = [
    {
        "asset_name": "MRI Scanner",
        "asset_type": "MRI",
        "category": "Medical Equipment",
        "manufacturer": "GE Healthcare"
    },
    {
        "asset_name": "CT Scanner",
        "asset_type": "CT Scanner",
        "category": "Medical Equipment",
        "manufacturer": "Siemens"
    },
    {
        "asset_name": "X-Ray Machine",
        "asset_type": "X-Ray",
        "category": "Medical Equipment",
        "manufacturer": "Philips"
    },
    {
        "asset_name": "Ventilator",
        "asset_type": "Ventilator",
        "category": "Life Support",
        "manufacturer": "Dräger"
    },
    {
        "asset_name": "Patient Monitor",
        "asset_type": "Monitor",
        "category": "Monitoring",
        "manufacturer": "Mindray"
    },
    {
        "asset_name": "ECG Machine",
        "asset_type": "ECG",
        "category": "Diagnostic",
        "manufacturer": "BPL"
    },
    {
        "asset_name": "Ultrasound Machine",
        "asset_type": "Ultrasound",
        "category": "Imaging",
        "manufacturer": "Samsung"
    },
    {
        "asset_name": "Infusion Pump",
        "asset_type": "Infusion Pump",
        "category": "Therapy",
        "manufacturer": "Baxter"
    },
    {
        "asset_name": "Defibrillator",
        "asset_type": "Defibrillator",
        "category": "Emergency",
        "manufacturer": "ZOLL"
    },
    {
        "asset_name": "HVAC Unit",
        "asset_type": "AHU",
        "category": "Infrastructure",
        "manufacturer": "Daikin"
    }
]

retail_assets = [
    {
        "asset_name": "POS Terminal",
        "asset_type": "POS",
        "category": "Sales",
        "manufacturer": "NCR"
    },
    {
        "asset_name": "Barcode Scanner",
        "asset_type": "Barcode Scanner",
        "category": "Sales",
        "manufacturer": "Zebra"
    },
    {
        "asset_name": "CCTV Camera",
        "asset_type": "CCTV",
        "category": "Security",
        "manufacturer": "Hikvision"
    },
    {
        "asset_name": "Digital Signage",
        "asset_type": "Display",
        "category": "Marketing",
        "manufacturer": "LG"
    },
    {
        "asset_name": "HVAC Unit",
        "asset_type": "AHU",
        "category": "Infrastructure",
        "manufacturer": "Daikin"
    },
    {
        "asset_name": "Escalator",
        "asset_type": "Escalator",
        "category": "Infrastructure",
        "manufacturer": "Otis"
    },
    {
        "asset_name": "UPS",
        "asset_type": "UPS",
        "category": "Power",
        "manufacturer": "APC"
    },
    {
        "asset_name": "Server Rack",
        "asset_type": "Server",
        "category": "IT",
        "manufacturer": "Dell"
    }
]

office_assets = [
    {
        "asset_name": "Desktop Computer",
        "asset_type": "Desktop",
        "category": "IT",
        "manufacturer": "Dell"
    },
    {
        "asset_name": "Conference Display",
        "asset_type": "Display",
        "category": "AV",
        "manufacturer": "Samsung"
    },
    {
        "asset_name": "Network Switch",
        "asset_type": "Network Switch",
        "category": "Networking",
        "manufacturer": "Cisco"
    },
    {
        "asset_name": "WiFi Access Point",
        "asset_type": "Access Point",
        "category": "Networking",
        "manufacturer": "Cisco"
    },
    {
        "asset_name": "UPS",
        "asset_type": "UPS",
        "category": "Power",
        "manufacturer": "APC"
    },
    {
        "asset_name": "HVAC Unit",
        "asset_type": "AHU",
        "category": "Infrastructure",
        "manufacturer": "Daikin"
    },
    {
        "asset_name": "Biometric Device",
        "asset_type": "Biometric",
        "category": "Security",
        "manufacturer": "ZKTeco"
    },
    {
        "asset_name": "Printer",
        "asset_type": "Printer",
        "category": "Office Equipment",
        "manufacturer": "HP"
    }
]

manufacturing_assets = [
    {
        "asset_name": "CNC Machine",
        "asset_type": "CNC",
        "category": "Production",
        "manufacturer": "Mazak"
    },
    {
        "asset_name": "Conveyor Belt",
        "asset_type": "Conveyor",
        "category": "Production",
        "manufacturer": "Siemens"
    },
    {
        "asset_name": "Industrial Robot",
        "asset_type": "Robot",
        "category": "Automation",
        "manufacturer": "ABB"
    },
    {
        "asset_name": "Air Compressor",
        "asset_type": "Compressor",
        "category": "Utilities",
        "manufacturer": "Atlas Copco"
    },
    {
        "asset_name": "Boiler",
        "asset_type": "Boiler",
        "category": "Utilities",
        "manufacturer": "Thermax"
    },
    {
        "asset_name": "Forklift",
        "asset_type": "Forklift",
        "category": "Material Handling",
        "manufacturer": "Toyota"
    },
    {
        "asset_name": "Generator",
        "asset_type": "Generator",
        "category": "Power",
        "manufacturer": "Cummins"
    },
    {
        "asset_name": "HVAC Unit",
        "asset_type": "AHU",
        "category": "Infrastructure",
        "manufacturer": "Daikin"
    }
]

hospitality_assets = [
    {
        "asset_name": "Reception Computer",
        "asset_type": "Desktop",
        "category": "IT",
        "manufacturer": "Dell"
    },
    {
        "asset_name": "Elevator",
        "asset_type": "Elevator",
        "category": "Infrastructure",
        "manufacturer": "Otis"
    },
    {
        "asset_name": "CCTV Camera",
        "asset_type": "CCTV",
        "category": "Security",
        "manufacturer": "Hikvision"
    },
    {
        "asset_name": "Laundry Machine",
        "asset_type": "Laundry Machine",
        "category": "Operations",
        "manufacturer": "LG"
    },
    {
        "asset_name": "Kitchen Oven",
        "asset_type": "Oven",
        "category": "Kitchen",
        "manufacturer": "Bosch"
    },
    {
        "asset_name": "HVAC Unit",
        "asset_type": "AHU",
        "category": "Infrastructure",
        "manufacturer": "Daikin"
    },
    {
        "asset_name": "UPS",
        "asset_type": "UPS",
        "category": "Power",
        "manufacturer": "APC"
    },
    {
        "asset_name": "Fire Alarm Panel",
        "asset_type": "Fire Alarm",
        "category": "Safety",
        "manufacturer": "Honeywell"
    }
]
# =====================================================
# Industry Asset Configuration
# =====================================================

industry_asset_config = {
    "Healthcare": healthcare_assets,
    "Retail": retail_assets,
    "Commercial Offices": office_assets,
    "Manufacturing": manufacturing_assets,
    "Hospitality": hospitality_assets
}

# =====================================================
# Building Configuration
# =====================================================

building_config = {
    "Healthcare": {
        "min_buildings": 2,
        "max_buildings": 5
    },

    "Retail": {
        "min_buildings": 1,
        "max_buildings": 3
    },

    "Commercial Offices": {
        "min_buildings": 2,
        "max_buildings": 6
    },

    "Manufacturing": {
        "min_buildings": 3,
        "max_buildings": 8
    },

    "Hospitality": {
        "min_buildings": 1,
        "max_buildings": 4
    }
}

industry_config = {
    "Healthcare": healthcare_site_pool,
    "Retail": retail_site_pool,
    "Commercial Offices": office_site_pool,
    "Manufacturing": manufacturing_site_pool,
    "Hospitality": hospitality_site_pool
}

print("Healthcare Site Pool :", len(healthcare_site_pool))
print("Retail Site Pool :", len(retail_site_pool))
print("Office Site Pool :", len(office_site_pool))
print("Manufacturing Site Pool :", len(manufacturing_site_pool))
print("Hospitality Site Pool :", len(hospitality_site_pool))   

sites = []

site_buildings = {}

site_counter = 1  

for customer in customers:

    number_of_sites = random.randint(
        customer["min_sites"],
        customer["max_sites"]
    )

    print("=" * 60)
    print(f"Customer : {customer['customer_name']}")
    print(f"Industry : {customer['industry']}")
    print(f"Sites to Generate : {number_of_sites}")

    for site_number in range(number_of_sites):
        site_pool = industry_config[customer["industry"]]

        site = site_pool.pop()

        city = site["city"]
        site_type = site["site_type"]
        site_name = site["site_name"]

        site_id = f"SITE{site_counter:03d}"

        

        site_record = {
           "site_id": site_id,
           "customer_id": customer["customer_id"],
           "customer_name": customer["customer_name"],
           "industry": customer["industry"],
           "city": city,
           "site_type": site_type,
           "site_name": site_name
}

        sites.append(site_record)
        site_counter += 1

sites_df = pd.DataFrame(sites)

print()
print("=" * 60)
print("Total Sites Generated :", len(sites_df))
print("=" * 60)


sites_df.to_csv(
    "data/raw/sites.csv",
    index=False
)
# =====================================================
# Generate Buildings
# =====================================================

building_records = []

for index, site in sites_df.iterrows():

    current_building_config = building_config[
        site["industry"]
    ]

    number_of_buildings = random.randint(
        current_building_config["min_buildings"],
        current_building_config["max_buildings"]
    )

    buildings = []

    for building_number in range(1, number_of_buildings + 1):

        building_id = (
            f"{site['site_id']}_BLDG{building_number:02d}"
        )

        buildings.append(building_id)

        building_records.append({

            "building_id": building_id,

            "site_id": site["site_id"],

            "building_name": f"Building {building_number}"

        })

    site_buildings[site["site_id"]] = buildings

buildings_df = pd.DataFrame(building_records)

print()
print("=" * 60)
print("Total Buildings Generated :", len(buildings_df))
print("=" * 60)

print(buildings_df.head())

buildings_df.to_csv(
    "data/raw/buildings.csv",
    index=False
)

print("\nBuildings Dataset saved successfully!")

def generate_installation_date():

    start_date = datetime(2019, 1, 1)

    end_date = datetime(2025, 12, 31)

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    installation_date = start_date + timedelta(days=random_days)

    return installation_date.date()

def generate_warranty_expiry(installation_date):

    warranty_expiry = installation_date + timedelta(days=365 * 5)

    return warranty_expiry
# =====================================================
# Generate Assets
# =====================================================

assets = []

asset_counter = 1
for index, site in sites_df.iterrows():

    number_of_assets = random.randint(20, 50)

    for asset_number in range(number_of_assets):

        asset_list = industry_asset_config[site["industry"]]

        asset = random.choice(asset_list)

        installation_date = generate_installation_date()

        warranty_expiry = generate_warranty_expiry(
            installation_date
        )

        building_id = random.choice(
             site_buildings[site["site_id"]]
        )

        asset_record = {
            "asset_id": f"ASSET{asset_counter:06d}",
            "site_id": site["site_id"],
            "building_id": building_id,
            "customer_id": site["customer_id"],
            "asset_type": asset["asset_type"],
            "asset_name": asset["asset_name"],
            "category": asset["category"],
            "manufacturer": asset["manufacturer"],
            "installation_date": installation_date,
            "warranty_expiry": warranty_expiry
        }

        assets.append(asset_record)

        asset_counter += 1

assets_df = pd.DataFrame(assets)

print()
print("=" * 60)
print("Site -> Buildings")
print("=" * 60)

for site_id, buildings in site_buildings.items():
    print(site_id, ":", buildings)

print()

print("=" * 60)
print("Total Assets Generated :", len(assets_df))
print("=" * 60)

print(assets_df.head())

assets_df.to_csv(
    "data/raw/assets.csv",
    index=False
)

print("\nAssets saved successfully!")

# =====================================================
# Create Asset Metadata Dataset
# =====================================================

asset_metadata_df = pd.merge(
    assets_df,
    sites_df,
    on="site_id",
    how="left",
    suffixes=("", "_site")
)


asset_metadata_df = asset_metadata_df[
    [
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
]

print()
print("=" * 60)
print("Asset Metadata Dataset")
print("=" * 60)

print(asset_metadata_df.head())

asset_metadata_df.to_csv(
    "data/raw/asset_metadata.csv",
    index=False
)

print("\nAsset Metadata Dataset saved successfully!")

# =====================================================
# Generate IoT Telemetry Dataset
# =====================================================

telemetry = []

sensor_counter = 1

for index, asset in asset_metadata_df.iterrows():

    sensor_id = f"SENSOR{sensor_counter:06d}"

    sensor_counter += 1

    base_temperature = random.uniform(20, 30)

    base_humidity = random.uniform(45, 65)

    base_pressure = random.uniform(995, 1015)

    base_vibration = random.uniform(0.5, 2.0)

    base_power = random.uniform(5, 10)

    for reading in range(100):
        start_time = datetime(2025, 7, 1, 8, 0, 0)

        timestamp = start_time + timedelta(minutes=reading * 5)

        operating_mode = random.choices(
            ["Running", "Idle", "Maintenance", "Shutdown"],
            weights=[70, 15, 10, 5],
            k=1
        )[0]

        if operating_mode == "Running":

            temperature = round(
                (base_temperature + 5) + random.uniform(-0.3, 0.3),
                2
            )

            humidity = round(
                base_humidity + random.uniform(-1, 1),
                2
            )

            pressure = round(
                base_pressure + random.uniform(-0.5, 0.5),
                2
            )

            vibration = round(
                (base_vibration + 1.0) + random.uniform(-0.1, 0.1),
                2
            )

            power_consumption = round(
                (base_power + 4) + random.uniform(-0.3, 0.3),
                2
            )

        elif operating_mode == "Idle":

            temperature = round(
                base_temperature + random.uniform(-0.3, 0.3),
                2
            )

            humidity = round(
                base_humidity + random.uniform(-1, 1),
                2
            )

            pressure = round(
                base_pressure + random.uniform(-0.5, 0.5),
                2
            )

            vibration = round(
                (base_vibration * 0.3) + random.uniform(-0.05, 0.05),
                2
            )

            power_consumption = round(
                (base_power * 0.3) + random.uniform(-0.2, 0.2),
                2
            )


        elif operating_mode == "Maintenance":

            temperature = round(
                22 + random.uniform(-0.3, 0.3),
                2
            )

            humidity = round(
                base_humidity + random.uniform(-1, 1),
                2
            )

            pressure = round(
                base_pressure + random.uniform(-0.5, 0.5),
                2
            )

            vibration = 0.00

            power_consumption = 0.20


        else:      # Shutdown

            temperature = round(
                22 + random.uniform(-0.2, 0.2),
                2
            )

            humidity = round(
                base_humidity + random.uniform(-1, 1),
                2
            )

            pressure = round(
                base_pressure + random.uniform(-0.5, 0.5),
                2
            )

            vibration = 0.00

            power_consumption = 0.00

# =====================================================
# Simulate Rare Anomalies (2% Probability)
# =====================================================

        if random.random() < 0.02:

            anomaly = random.choice(
        [
            "High Temperature",
            "High Vibration",
            "Power Spike"
        ]
        )

            if anomaly == "High Temperature":
                temperature += random.uniform(8, 15)

            elif anomaly == "High Vibration":
                vibration += random.uniform(2, 4)

            elif anomaly == "Power Spike":
                power_consumption += random.uniform(5, 10)

        telemetry_record = {

            "timestamp": timestamp,

            "site_id": asset["site_id"],

            "building_id": asset["building_id"],

            "asset_id": asset["asset_id"],

            "sensor_id": sensor_id,

            "temperature": temperature,

            "humidity": humidity,

            "pressure": pressure,

            "vibration": vibration,

            "power_consumption": power_consumption,

            "operating_mode": operating_mode

        }

        telemetry.append(telemetry_record)

telemetry_df = pd.DataFrame(telemetry)

print()
print("=" * 60)
print("IoT Telemetry Dataset")
print("=" * 60)

print("Total Telemetry Records Generated :", len(telemetry_df))

print()

print(telemetry_df.head())

telemetry_df.to_csv(
    "data/raw/iot_telemetry.csv",
    index=False
)

print("\nIoT Telemetry Dataset saved successfully!")  

# =====================================================
# Generate Event Dataset
# =====================================================

asset_lookup = dict(
    zip(asset_metadata_df["asset_id"], asset_metadata_df["asset_name"])
)
events = []

event_counter = 1

for index, row in telemetry_df.iterrows():

        asset_name = asset_lookup[row["asset_id"]]

        event_type = None
        severity = None
        message = None

        if row["temperature"] > 38:

           event_type = "Alarm"

           severity = "High"

           message = f"High temperature detected in {asset_name}."

        elif row["vibration"] > 3:

           event_type = "Fault"

           severity = "High"

           message = f"Excessive vibration detected in {asset_name}."

        elif row["power_consumption"] > 14:

           event_type = "Alarm"

           severity = "Medium"

           message = f"Abnormal power consumption detected in {asset_name}."

        elif row["operating_mode"] == "Maintenance":

           event_type = "Warning"

           severity = "Low"

           message = f"{asset_name} is undergoing scheduled maintenance."

        elif row["operating_mode"] == "Shutdown":

           event_type = "Warning"

           severity = "Medium"

           message = f"{asset_name} has been shut down."

        if event_type is not None:

            asset_name = asset_metadata_df.loc[
                asset_metadata_df["asset_id"] == row["asset_id"],
                "asset_name"
            ].values[0]

            event_record = {

                "event_id": f"EVT{event_counter:06d}",

                "timestamp": row["timestamp"],

                "asset_id": row["asset_id"],

                "event_type": event_type,

                "severity": severity,

                "message": message

            }

            events.append(event_record)

            event_counter += 1

events_df = pd.DataFrame(events)

print()
print("=" * 60)
print("Event Dataset")
print("=" * 60)

print("Total Events Generated :", len(events_df))

print()

print(events_df.head())

events_df.to_csv(
    "data/raw/event_data.csv",
    index=False
)

print("\nEvent Dataset saved successfully!")