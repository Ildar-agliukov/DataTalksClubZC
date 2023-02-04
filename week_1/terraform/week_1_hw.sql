-- How many taxi trips were totally made on January 15?

select
  count(*) as cnt
from public.newtable_1 n
where n.lpep_pickup_datetime::date = '2019-01-15' and n.lpep_dropoff_datetime::date = '2019-01-15'
;

-- Which was the day with the largest trip distance?
select lpep_pickup_datetime::date from public.newtable_1 n order by trip_distance desc limit 1;

-- In 2019-01-01 how many trips had 2 and 3 passengers?
select passenger_count, count(*) from public.newtable_1 n where n.passenger_count in (2, 3) and n.lpep_pickup_datetime::date = '2019-01-01' group by passenger_count;

-- For the passengers picked up in the Astoria Zone which was the drop up zone that had the largest tip?
select n3."Zone" as drop_up_zone
from public.newtable_1 n
  left join newtable n2 on n2.locationid = n.pulocationid
  left join newtable n3 on n.dolocationid = n3.locationid 
where n2."Zone" = 'Astoria'
order by tip_amount desc 
limit 1;
