# Data preparation
you can the code that parse data from git and upload it to gsc in from_git_to_gcs.py script

To create the tables I wrote next code in biq query sql console
```sql
CREATE OR REPLACE TABLE `trips_data_all.week3_external`
OPTIONS (
   format = 'CSV',
   uris = ['gs://dtc_data_lake_global-agliukov/week3/2019-*']
);

CREATE OR REPLACE TABLE `trips_data_all.week3_bq` AS
SELECT * FROM trips_data_all.week3_external;
```

# Task 1
```sql
SELECT COUNT(*) FROM trips_data_all.week3_external
```
___
# Task 2
```sql
SELECT COUNT(*) FROM trips_data_all.week3_external
```
gives 0 bytes

and 
```sql
SELECT COUNT(*) FROM trips_data_all.week3_bq
```
gives the same size
___
# Task 3
```sql
SELECT  
    count(*) as total_rows
FROM `global-agliukov.trips_data_all.week3_bq`
where PUlocationID IS NULL AND DOlocationID IS NULL
```
___

# Task 4

Partition by pickup_datetime Cluster on affiliated_base_number
___
# Task 5
```sql
CREATE OR REPLACE TABLE `trips_data_all.week3_partitioned` 
PARTITION BY
  DATE(pickup_datetime) AS
SELECT * FROM `trips_data_all.week3_bq`
```

