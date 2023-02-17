from datetime import date
from io import BytesIO
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
import requests
from dateutil.relativedelta import relativedelta
from google.cloud import storage

@task(cache_result_in_memory=True)
def fetch(url: str) -> BytesIO:
    """get data from link and return data as a file type object"""
    request = requests.get(url)
    return BytesIO(request.content)


@task(retries=5, retry_delay_seconds=60)
def to_gc(file: BytesIO, path: str) -> None:
    """upload data to google cloud storage"""
    file.seek(0)
    client = storage.Client()
    bucket = client.bucket('dtc_data_lake_global-agliukov')
    blob = bucket.blob(f"week4/{path}.csv.gz")
    blob.upload_from_file(file, timeout=600)


@flow(log_prints=True)
def main_flow() -> None:
    """get data from github and push it to the google cloud storage"""
    start:date = date(2019, 1, 1)
    finish:date = date(2021, 8, 1)
    while start < finish:
        c_date = start.strftime("%Y-%m")
        data = fetch(f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_{c_date}.csv.gz')
        to_gc(data, 'yellow_3' + c_date)
        start += relativedelta(months=1)
    

if __name__ == '__main__':
    main_flow()
