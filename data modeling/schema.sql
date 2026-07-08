-- =====================================================
-- Nectar Data Engineering Assignment
-- Task 3 - Data Modeling
-- Star Schema Design
-- =====================================================
-- =====================================================
-- Dimension Table : Site
-- =====================================================

CREATE TABLE dim_site (

    site_id VARCHAR(20) PRIMARY KEY,

    customer_id VARCHAR(20),

    customer_name VARCHAR(100),

    industry VARCHAR(50),

    city VARCHAR(50),

    site_type VARCHAR(50),

    site_name VARCHAR(100)

);

-- =====================================================
-- Dimension Table : Building
-- =====================================================

CREATE TABLE dim_building (

    building_id VARCHAR(20) PRIMARY KEY,

    site_id VARCHAR(20) NOT NULL,

    building_name VARCHAR(100) NOT NULL,

    FOREIGN KEY (site_id)
        REFERENCES dim_site(site_id)

);

-- =====================================================
-- Dimension Table : Asset
-- =====================================================

CREATE TABLE dim_asset (

    asset_id VARCHAR(20) PRIMARY KEY,

    building_id VARCHAR(20) NOT NULL,

    site_id VARCHAR(20) NOT NULL,

    customer_id VARCHAR(20),

    asset_name VARCHAR(100) NOT NULL,

    asset_type VARCHAR(50) NOT NULL,

    category VARCHAR(50),

    manufacturer VARCHAR(100),

    installation_date DATE,

    warranty_expiry DATE,

    FOREIGN KEY (building_id)
        REFERENCES dim_building(building_id),

    FOREIGN KEY (site_id)
        REFERENCES dim_site(site_id)

);

-- =====================================================
-- Dimension Table : Time
-- =====================================================

CREATE TABLE dim_time (

    time_id VARCHAR(20) PRIMARY KEY,

    full_date TIMESTAMP NOT NULL,

    hour INT NOT NULL,

    day INT NOT NULL,

    month INT NOT NULL,

    quarter INT NOT NULL,

    year INT NOT NULL,

    weekday VARCHAR(20) NOT NULL

);


-- =====================================================
-- Fact Table : Telemetry
-- =====================================================

CCREATE TABLE fact_telemetry (

    telemetry_id BIGSERIAL PRIMARY KEY,

    timestamp TIMESTAMP NOT NULL,

    site_id VARCHAR(20),

    building_id VARCHAR(20),

    asset_id VARCHAR(20),

    sensor_id VARCHAR(20),

    temperature DECIMAL(8,2),

    humidity DECIMAL(8,2),

    pressure DECIMAL(8,2),

    vibration DECIMAL(8,2),

    power_consumption DECIMAL(10,2),

    operating_mode VARCHAR(30)

);

-- =====================================================
-- Fact Table : Event
-- =====================================================

CREATE TABLE fact_event (

    event_id VARCHAR(20) PRIMARY KEY,

    timestamp TIMESTAMP,

    asset_id VARCHAR(20),

    event_type VARCHAR(50),

    severity VARCHAR(20),

    message VARCHAR(255)

);


-- =====================================================
-- Fact Table : Energy
-- =====================================================

CREATE TABLE fact_energy (

    energy_id BIGSERIAL PRIMARY KEY,

    date DATE,

    hour INTEGER,

    hourly_energy_consumption DECIMAL(12,2)

);

-- =====================================================
-- Fact Table : Asset Health
-- =====================================================

CREATE TABLE fact_asset_health (

    asset_id VARCHAR(20) PRIMARY KEY,

    total_energy DECIMAL(12,2),

    average_power DECIMAL(10,2),

    average_temperature DECIMAL(8,2),

    average_humidity DECIMAL(8,2),

    average_pressure DECIMAL(10,2),

    average_vibration DECIMAL(8,2),

    total_faults INTEGER,

    health_score DECIMAL(5,2),

    risk_level VARCHAR(20)

);

-- =====================================================
-- Fact Table : Maintenance
-- =====================================================

