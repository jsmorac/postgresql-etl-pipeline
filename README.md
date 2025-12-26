# Data Engineer Technical Assessment -- VIP Medical Group

This repository contains a data engineering solution developed as part
of a technical assessment. The objective is to ingest, clean, and load
healthcare-related data into a PostgreSQL database following good
engineering practices.

------------------------------------------------------------------------

## Project Overview

The project implements an ETL (Extract, Transform, Load)
pipeline that:

-   Reads raw Excel files containing appointment and doctor information
-   Cleans and standardizes the data
-   Handles data quality issues gracefully
-   Loads the processed data into a PostgreSQL database

An exploratory notebook is also included to document data quality
findings and design decisions prior to building the ETL pipeline.

------------------------------------------------------------------------

## Project Structure

    RedValley/
    │
    ├── data/
    │   ├── raw/              # Original Excel files
    │   └── processed/        # Final cleaned datasets
    │
    ├── notebooks/
    │   └── 01_data_exploration.ipynb
    │
    ├── src/
    │   ├── config.py         # Configuration and paths
    │   ├── db.py             # PostgreSQL connection
    │   ├── transform.py      # Data cleaning and transformations
    │   └── etl.py            # Main ETL pipeline
    │
    ├── queries.sql           # SQL queries for business questions
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Datasets

The following datasets were provided:

-   **Appointments dataset**
    -   Contains booking information, patient IDs, doctor IDs, dates,
        and appointment status.
-   **Doctors dataset**
    -   Contains doctor identifiers, names, and specialties.

Both datasets are located in the data/raw/ directory.

------------------------------------------------------------------------

## Data Exploration

An exploratory analysis was performed before building the ETL pipeline.
See: `notebooks/01_data_exploration.ipynb`

### Key findings:

-   Non-numeric values were found in `booking_id` (e.g., '37X')
-   Appointment status values were inconsistent (e.g., confirmed,
    Confirmed, confirmed.)
-   One `doctor_id` referenced in appointments does not exist in the
    doctors dataset
-   A significant number of `booking_date` values were invalid or
    inconsistent
-   No duplicated rows were found in either dataset

These findings directly informed the transformation logic implemented in
the ETL pipeline.

------------------------------------------------------------------------

## ETL Pipeline

### Extract

-   Raw Excel files are read using pandas

### Transform

-   Invalid `booking_id` values coerced and removed
-   Appointment status values are normalized
-   Dates are parsed safely (`errors='coerce'`)
-   Nullable fields are handled explicitly
-   Referential integrity enforced (appointments with invalid doctor_id dropped)
-   Data quality issues are logged for transparency

### Load

-   Cleaned data is loaded into a local `PostgreSQL` database using
    `SQLAlchemy`
-   Tables are created in the `healthtech` schema using `to_sql`

------------------------------------------------------------------------

## Final Dataset

Before loading into PostgreSQL, the cleaned datasets are saved in:

- `data/processed/doctors.csv`
- `data/processed/appointments.csv`

These files represent the final dataset deliverable.

------------------------------------------------------------------------

## Requirements

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## How to Run

1.  Ensure PostgreSQL is running locally
2.  Update database credentials in `src/config.py` if needed
3.  Run the ETL pipeline from the project root:

``` bash
python src/etl.py
```
Logs will be printed to the console during execution.

------------------------------------------------------------------------

## Database Credentials

For simplicity in this technical assessment, default credentials are hardcoded in src/config.py:

- host: localhost
- port: 5432
- dbname: postgres
- user: postgres
- password: sebastian7

In production environments, credentials should never be hardcoded.
Instead, they should be set via environment variables or a secrets manager.

------------------------------------------------------------------------

## Queries

Business questions are answered in `queries.sql` at the project root.
To execute:

1. 	Open pgAdmin and connect to your database
2. 	Open Query Tool
3. 	Copy-paste the queries from `queries.sql`
4. 	Run them to see results

------------------------------------------------------------------------

## Design Considerations

-   ETL implemented in Python scripts for reproducibility
-   Notebook used only for exploration/documentation
-   Logging tracks data quality issues instead of failing pipeline
-   Solution prioritizes clarity, robustness, and maintainability

------------------------------------------------------------------------
## AWS Architecture Proposal

In production, the ETL pipeline would use AWS managed services:

### Extract
- **Amazon S3**: store raw file

### Transform
- **AWS Glue**: clean and transform data

### Load
- **Amazon RDS (PostgreSQL)**: store transformed data

### Orchestration
- **AWS Step Functions** or **Amazon Managed Airflow**: orchestrate workflow

This ensures scalability, security, and maintainability.

------------------------------------------------------------------------
## Potential Improvements

-   Enforce referential integrity between tables using foreign keys
-   Add automated data validation checks
-   Introduce incremental loads instead of full replacements
-   Containerize the solution using Docker

------------------------------------------------------------------------

## Author

**Jhoan Mora**
