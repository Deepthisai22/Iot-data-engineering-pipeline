-- =====================================================
-- Asset Connectivity Bridge Table
-- =====================================================

CREATE TABLE asset_connectivity (

    connection_id SERIAL PRIMARY KEY,

    parent_asset_id VARCHAR(20) NOT NULL,

    child_asset_id VARCHAR(20) NOT NULL,

    connection_type VARCHAR(30),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (parent_asset_id)
        REFERENCES dim_asset(asset_id),

    FOREIGN KEY (child_asset_id)
        REFERENCES dim_asset(asset_id)

);