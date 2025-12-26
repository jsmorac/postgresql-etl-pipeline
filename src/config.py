"""
Configuration file for the ETL pipeline.

Includes:
- Project paths (raw, processed, logs)
- Input Excel files
- PostgreSQL connection settings
- Target schema name

Note: Database credentials can be set via environment variables.
"""


from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_FINAL_DIR = BASE_DIR / "data" / "processed"
LOGS_DIR = BASE_DIR / "logs"

APPOINTMENTS_FILE = DATA_RAW_DIR / "Data Engineer's Appointments Excel - VIP Medical Group.xlsx"
DOCTORS_FILE = DATA_RAW_DIR / "Data Enginner's Doctors Excel - VIP Medical Group.xlsx"

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "sebastian7")
}

SCHEMA_NAME = "healthtech"
