#All paths to location of my container & storage for tables

STORAGE_ACCOUNT = "devstorage242"
CONTAINER = "warehouse"

BASE_PATH = f"abfss://{CONTAINER}@{STORAGE_ACCOUNT}.dfs.core.windows.net/"

# Databricks Secrets

SECRET_SCOPE = "dataplatform-secrets"
SECRET_KEY = "storage-account-key"

#Dataset configurations

CONFIG = {


    "datasets": {
        "airlines": {
            "paths": {
                "bronze_base": "airlines/bronze",
                "silver_base": "airlines/silver",
                "gold_base": "airlines/gold",
                "raw_base": "airlines/raw"
            },
            "format": "csv",
            "tables": {
                "bronze": "bronze_airline_departures",
                "silver": "silver_airline_departures",
                "gold": {
                    "delays": "fact_airline_delays"
                }
            }
        }
    }
}