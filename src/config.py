from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_FINAL_DIR = BASE_DIR / "data" / "processed"
LOGS_DIR = BASE_DIR / "logs"

APPOINTMENTS_FILE = DATA_RAW_DIR / "Appointments excel.xlsx"
DOCTORS_FILE = DATA_RAW_DIR / "Doctors excel.xlsx"

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "")
}

SCHEMA_NAME = "healthtech"