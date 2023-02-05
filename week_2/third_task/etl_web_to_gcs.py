from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from random import randint


@task(retries=3)
def fetch(dataset_url: str) -> pd.DataFrame:
    """Read taxi data from web into pandas DataFrame"""
    df = pd.read_csv(dataset_url)
    return df


@task(log_prints=True)
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Fix dtype issues"""
    # print(df.columns)
    df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
    df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])
    # print(df.head(2))
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df


@task(retries=3)
def write_local(df: pd.DataFrame, color: str, path: Path) -> None:
    """Write DataFrame out locally as parquet file"""
    df.to_parquet(path, compression="gzip")


@task(retries=10)
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("zoom-gcp")
    gcs_block.upload_from_path(from_path=path, to_path=path)



@flow()
def etl_web_to_gcs(year: int, month: int, color: str) -> None:
    """The main ETL function"""
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"
    # df = fetch(dataset_url)
    # df_clean = clean(df)
    path = Path(f"data/{color}/{dataset_file}.parquet")
    # write_local(df_clean, color, path)
    write_gcs(path)


@flow(log_prints=True)
def etl_parent_flow(
     months: list[int] = [3], year: int = 2019, color: str = "yellow"
):
    for month in months:
        etl_web_to_gcs(year, month, color)
        

if __name__ == "__main__":
    etl_parent_flow()
    # etl_web_to_gcs()
