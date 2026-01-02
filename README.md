# Healthcare ETL Pipeline (PostgreSQL)

This repository contains a data engineering solution to ingest, clean, 
and load healthcare-related data into a PostgreSQL database following good 
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

    PostgreSQL-ETL/
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

## ETL Pipeline
- **Extract:** Raw Excel files are read using pandas.
- **Transform:** Invalid booking_id removed, appointment status normalized, dates parsed safely, referential integrity enforced, data quality issues logged.
- **Load:** Cleaned data loaded into PostgreSQL using SQLAlchemy (schema: `healthtech`).

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

Database credentials are loaded from environment variables for security:

- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`

------------------------------------------------------------------------

## Queries

Business questions are answered in `queries.sql` at the project root.
To execute:

1. 	Open pgAdmin and connect to your database
2. 	Open Query Tool
3. 	Copy-paste the queries from `queries.sql`
4. 	Run them to see results

------------------------------------------------------------------------
## AWS Architecture Proposal

In production, the ETL pipeline could use AWS managed services:

- Extract: Amazon S3
- Transform: AWS Glue
- Load: Amazon RDS (PostgreSQL)
- Orchestration: AWS Step Functions or Amazon Managed Airflow

------------------------------------------------------------------------
## Potential Improvements

-   Enforce referential integrity between tables using foreign keys
-   Add automated data validation checks
-   Introduce incremental loads instead of full replacements
-   Containerize the solution using Docker

------------------------------------------------------------------------

## Author

**Jhoan Mora**
