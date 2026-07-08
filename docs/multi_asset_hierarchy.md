# Multi-Asset Hierarchy & Connectivity

## Objective

Represent hierarchical relationships between connected IoT assets.

Example:

Site
 └── Building
      ├── Chiller
      │     ├── AHU-01
      │     └── AHU-02
      └── Pump
            └── Flow Sensor

---

## Relational Model

Create a bridge table named:

asset_connectivity

| Column | Description |
|---------|-------------|
| connection_id | Primary Key |
| parent_asset_id | Parent Asset |
| child_asset_id | Child Asset |
| connection_type | Physical / Logical |
| created_at | Connection Created Date |

Relationship:

dim_asset.asset_id
        |
        | parent_asset_id
        |
asset_connectivity
        |
        | child_asset_id
        |
dim_asset.asset_id

---

## Purpose

This bridge table supports

- Parent assets
- Child assets
- Asset hierarchy
- Connectivity mapping
- Graph traversal using SQL

---

# Sample SQL Queries

---

## 1. Retrieve all assets under a site

```sql
SELECT *
FROM dim_asset
WHERE site_id = 'SITE00001';
```

---

## 2. Retrieve parent and child assets

```sql
SELECT
    parent_asset_id,
    child_asset_id
FROM asset_connectivity;
```

---

## 3. Find downstream impacted assets

```sql
SELECT
    child_asset_id
FROM asset_connectivity
WHERE parent_asset_id = 'ASSET00001';
```

---

## 4. Identify orphan assets

```sql
SELECT
    asset_id
FROM dim_asset
WHERE asset_id NOT IN
(
    SELECT child_asset_id
    FROM asset_connectivity
);
```

---

## 5. Identify disconnected assets

```sql
SELECT
    asset_id
FROM dim_asset
WHERE asset_id NOT IN
(
    SELECT parent_asset_id
    FROM asset_connectivity
)
AND asset_id NOT IN
(
    SELECT child_asset_id
    FROM asset_connectivity
);
```

---

## Summary

This design uses a bridge table named **asset_connectivity** to model hierarchical relationships between IoT assets.

The solution supports:

- Retrieve all assets under a site
- Retrieve parent and child assets
- Find downstream impacted assets
- Identify orphan assets
- Identify disconnected assets

This relational model is scalable and can be extended to support complex asset hierarchies across multiple customer sites.