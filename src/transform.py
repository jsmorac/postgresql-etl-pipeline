"""
Data transformation functions.

Includes:
- Cleaning and normalization for doctors dataset
- Cleaning, validation, and normalization for appointments dataset
"""

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def transform_doctors(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["doctor_id"] = df["doctor_id"].astype(int)
    df["name"] = df["name"].str.strip()
    df["specialty"] = df["specialty"].str.strip()

    return df


def normalize_status(status: str) -> str:
    if pd.isna(status):
        return None

    status = status.lower().strip().replace(".", "")
    mapping = {
        "confirmed": "confirmed",
        "confirm": "confirmed",
        "canceled": "cancelled",
        "cancelled": "cancelled"
    }
    return mapping.get(status, status)


def transform_appointments(df: pd.DataFrame, valid_doctors: set) -> pd.DataFrame:
    df = df.copy()

    # booking_id seguro
    df["booking_id"] = pd.to_numeric(df["booking_id"], errors="coerce")
    invalid_ids = df["booking_id"].isna().sum()
    if invalid_ids > 0:
        logger.warning(f"{invalid_ids} records with invalid booking_id were dropped")

    df = df.dropna(subset=["booking_id"])
    df["booking_id"] = df["booking_id"].astype(int)

    # patient_id nullable
    df["patient_id"] = df["patient_id"].astype("Int64")

    # doctor_id
    df["doctor_id"] = df["doctor_id"].astype(int)

    # referential integrity: solo doctores válidos
    invalid_doctors = df.loc[~df["doctor_id"].isin(valid_doctors)]
    if not invalid_doctors.empty:
        logger.warning(f"{len(invalid_doctors)} records with invalid doctor_id were dropped")
        df = df[df["doctor_id"].isin(valid_doctors)]

    # dates
    df["booking_date"] = pd.to_datetime(df["booking_date"], errors="coerce")
    invalid_dates = df["booking_date"].isna().sum()
    if invalid_dates > 0:
        logger.warning(f"{invalid_dates} records with invalid booking_date")

    # status
    df["status"] = df["status"].apply(normalize_status)

    return df