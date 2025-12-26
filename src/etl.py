"""
Main ETL pipeline script.

Steps:
- Extract: read raw Excel files
- Transform: clean and normalize data
- Save: write processed datasets to data/processed
- Load: insert cleaned data into PostgreSQL (schema: healthtech)

Logs are written to console and logs/etl.log.
"""

import logging
import pandas as pd

from config import APPOINTMENTS_FILE, DOCTORS_FILE, SCHEMA_NAME
from transform import transform_doctors, transform_appointments
from db import get_engine
from sqlalchemy import text

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs/etl.log", mode="a")
    ]
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting ETL process")

    # Extract
    df_doctors = pd.read_excel(DOCTORS_FILE)
    df_appointments = pd.read_excel(APPOINTMENTS_FILE)

    logger.info(f"Doctors raw shape: {df_doctors.shape}")
    logger.info(f"Appointments raw shape: {df_appointments.shape}")

    # Transform
    df_doctors_clean = transform_doctors(df_doctors)
    valid_doctors = set(df_doctors_clean["doctor_id"])
    df_appointments_clean = transform_appointments(df_appointments, valid_doctors)

    # Save datasets
    df_doctors_clean.to_csv("data/processed/doctors.csv", index=False)
    df_appointments_clean.to_csv("data/processed/appointments.csv", index=False)


    # Load to PostgreSQL
    engine = get_engine()

    # Create schema if no exists
    with engine.begin() as conn:
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {SCHEMA_NAME}"))

    # Load tables into target schema
    df_doctors_clean.to_sql(
        "doctors",
        engine,
        schema=SCHEMA_NAME,
        if_exists="replace",
        index=False
    )

    df_appointments_clean.to_sql(
        "appointments",
        engine,
        schema=SCHEMA_NAME,
        if_exists="replace",
        index=False
    )

    logger.info("ETL process completed successfully")


if __name__ == "__main__":
    main()