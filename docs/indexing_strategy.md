# Indexing Strategy

## Overview

Indexes improve query performance by reducing the amount of data scanned during analytical queries. Since the IoT data warehouse stores large volumes of telemetry and event data, appropriate indexing is essential for efficient reporting and dashboard performance.

---

# Primary Key Indexes

The following primary keys are automatically indexed by PostgreSQL.

| Table | Primary Key |
|--------|-------------|
| dim_site | site_id |
| dim_building | building_id |
| dim_asset | asset_id |
| dim_time | time_id |
| fact_telemetry | telemetry_id |
| fact_event | event_id |
| fact_energy | energy_id |
| fact_asset_health | asset_id |

---

# Foreign Key Indexes

Indexes are created on frequently joined foreign key columns.

| Table | Indexed Column |
|--------|----------------|
| dim_building | site_id |
| dim_asset | site_id |
| dim_asset | building_id |
| dim_asset | customer_id |
| fact_telemetry | asset_id |
| fact_event | asset_id |
| fact_asset_health | asset_id |

---

# Time-Based Indexes

Time-based analytical queries are common in IoT systems.

Recommended indexes:

- timestamp (Telemetry)
- timestamp (Events)
- full_date (Time Dimension)

These indexes improve:

- Time-series analysis
- Daily reports
- Monthly reports
- Trend analysis

---

# Analytical Indexes

Frequently filtered columns should also be indexed.

## fact_telemetry

- operating_mode
- sensor_id

## fact_event

- event_type
- severity

## fact_asset_health

- health_score
- risk_level

## dim_asset

- asset_type
- manufacturer
- category

---

# Benefits

The indexing strategy provides:

- Faster JOIN operations
- Improved dashboard performance
- Reduced query execution time
- Efficient filtering on large datasets
- Better scalability for growing IoT data

---

# Summary

This indexing strategy supports high-performance analytical workloads by optimizing joins, filtering, and time-series queries across the IoT data warehouse.