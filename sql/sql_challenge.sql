-- =====================================================
-- Nectar Data Engineer Challenge
-- Task 6 : SQL Challenge
-- =====================================================

-- =====================================================
-- Question 1
-- Top 10 Assets with Highest Energy Consumption
-- =====================================================

SELECT
    asset_id,
    SUM(hourly_energy) AS total_energy
FROM fact_energy
GROUP BY asset_id
ORDER BY total_energy DESC
LIMIT 10;

-- =====================================================
-- Question 2
-- Average Daily Energy Consumption for Each Site
-- =====================================================

SELECT
    site_id,
    DATE(timestamp) AS day,
    AVG(power_consumption) AS average_daily_energy
FROM fact_telemetry
GROUP BY site_id, DATE(timestamp)
ORDER BY site_id, day;

-- =====================================================
-- Question 3
-- Assets with More Than 10 Faults in Last 30 Days
-- =====================================================

SELECT
    asset_id,
    COUNT(*) AS total_faults
FROM fact_event
WHERE timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY asset_id
HAVING COUNT(*) > 10
ORDER BY total_faults DESC;

-- =====================================================
-- Question 4
-- Assets Without Telemetry in Last 24 Hours
-- =====================================================

SELECT asset_id
FROM dim_asset
WHERE asset_id NOT IN (
    SELECT DISTINCT asset_id
    FROM fact_telemetry
    WHERE timestamp >= NOW() - INTERVAL '24 hours'
);

-- =====================================================
-- Question 5
-- Calculate Hourly Utilization for Each Building
-- =====================================================

SELECT
    building_id,
    DATE(timestamp) AS day,
    EXTRACT(HOUR FROM timestamp) AS hour,
    AVG(power_consumption) AS average_hourly_utilization
FROM fact_telemetry
GROUP BY
    building_id,
    DATE(timestamp),
    EXTRACT(HOUR FROM timestamp)
ORDER BY
    building_id,
    day,
    hour;


	-- =====================================================
-- Question 6
-- Identify Sites with Abnormal Power Consumption
-- =====================================================

SELECT
    site_id,
    AVG(power_consumption) AS average_power,
    MAX(power_consumption) AS peak_power
FROM fact_telemetry
GROUP BY site_id
HAVING MAX(power_consumption) > AVG(power_consumption) * 1.5
ORDER BY peak_power DESC;
