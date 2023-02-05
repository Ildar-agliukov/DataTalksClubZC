from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
from prefect.tasks import task_input_hash
from datetime import timedelta


@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> pd.DataFrame:
    """Download trip data from GCS"""
    gcs_path = f"data/{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcs_block = GcsBucket.load("zoom-gcp")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"data/")
    return pd.read_parquet(f"data/{gcs_path}")


@task(log_prints=True)
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("gcp-cred")

    df.to_gbq(
        destination_table="trips_data_all.rides_2",
        project_id="global-agliukov",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="replace",
    )


@flow(log_prints=True)
def etl_gcs_to_bq(color, year, month):
    """Main ETL flow to load data into Big Query"""
    df = extract_from_gcs(color, year, month)
    print(f"rows: {len(df)}")
    write_bq(df)


@flow(log_prints=True)
def etl_parent_flow(
     months: list[int] = [2, 3], year: int = 2019, color: str = "yellow"
):
    for month in months:
        etl_gcs_to_bq(color, year, month)


if __name__ == "__main__":
    etl_parent_flow()
