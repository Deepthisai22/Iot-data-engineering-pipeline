# Partitioning Strategy

## Overview

The IoT platform generates high-volume telemetry and event data continuously. To improve query performance, simplify maintenance, and support historical analytics, partitioning is applied to the large fact tables.

---

# Partitioning Approach

The fact tables are partitioned by time using the `time_id` attribute.

This approach provides:

- Faster query performance
- Efficient historical reporting
- Simplified maintenance
- Easier archival of old data

---

# Tables to Partition

## fact_telemetry

Partition Type:

- Range Partition

Partition Key:

- time_id

Reason:

Telemetry data is generated every few minutes and grows rapidly. Most analytical queries filter by date or time.

---

## fact_event

Partition Type:

- Range Partition

Partition Key:

- time_id

Reason:

Event logs are typically queried by day, week, or month. Time-based partitioning reduces scan time.

---

## fact_energy

Partition Type:

- Range Partition

Partition Key:

- time_id

Reason:

Energy consumption is analyzed over hourly, daily, and monthly intervals.

---

## fact_asset_health

Partition Type:

- Range Partition

Partition Key:

- time_id

Reason:

Asset health scores are monitored over time to identify trends and support predictive maintenance.

---

# Example Monthly Partitions

fact_telemetry

- telemetry_2025_07
- telemetry_2025_08
- telemetry_2025_09

fact_event

- event_2025_07
- event_2025_08
- event_2025_09

fact_energy

- energy_2025_07
- energy_2025_08
- energy_2025_09

fact_asset_health

- asset_health_2025_07
- asset_health_2025_08
- asset_health_2025_09

---

# Benefits

- Faster dashboard queries
- Reduced disk scanning
- Better query optimization
- Efficient archival of historical data
- Improved scalability for large IoT datasets