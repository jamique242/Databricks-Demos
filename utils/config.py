CONFIG = {
    "paths": {
        "bronze_base": "/mnt/bronze",
        "silver_base": "/mnt/silver",
        "gold_base": "/mnt/gold",
        "raw_base": "/mnt/raw"
    },

    "datasets": {
        "airlines": {
            "source": {
                "path": "/mnt/raw/airlines",
                "format": "csv"
            },
            "tables": {
                "bronze": "datahive.bronze_airline_departures",
                "silver": "datahive.silver_airline_departures",
                "gold": {
                    "delays": "datahive.fact_airline_delays"
                }
            }
        }
    }
}