# First task
In first task we change variables in etl_web_to_gcs flow:
* Color from yellow to green, 
* Year from 2021 to 2020 

```python
color = "green"
year = 2020
```

Also we have to change the column prefix from **tpep** to **lpep**

```python
df["lpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["lpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
```
___
# Second task

0 5 1 * *

by clt i build the deployment_file

```bash
prefect deployment build etl_web_to_gcs.py:etl_web_to_gcs -n "etl_with_cron" --cron "0 5 1 * *"
```
and the file was added to the perfect by
```bash
prefect deployment apply etl_web_to_gcs-deployment.yaml
```
___
# Third task

I sumed the printed row number.

files in folder

___
# Code for task four and five in folders
