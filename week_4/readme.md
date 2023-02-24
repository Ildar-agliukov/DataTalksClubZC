Data imported to BIG QUERY from Google cloud storage.

data to google cloud storage was uploaded by from_git_to_gcs.pu script

# Task 1

```sql
SELECT count(*) FROM `fact_trips`
WHERE EXTRACT(YEAR FROM pickup_datetime) IN (2019, 2020) 
```
___
# Task 2

89.9/10.1

___
# Task 3

```sql
SELECT count(*) FROM `stg_fhv_tripdata`
where extract(year from pickup_datetime) = 2019
```

# Task 4
```sql
SELECT count(*) FROM `fact_fhv_trips`
where extract(year from pickup_datetime) = 2019
```
# Task 5
simpe dash
https://lookerstudio.google.com/reporting/c3dd96c7-97bf-45a7-a73e-4d1769fccddf
