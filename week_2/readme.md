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