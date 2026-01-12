# Write your MySQL query statement below
## 2 cte 1 for first half, second for H2
with h1_avg_raw as (
    select 
    driver_id,
    avg(distance_km / fuel_consumed) as first_half_avg
    from trips
    where trip_date between date '2023-01-01' and last_day('2023-06-01')
    group by 1
), h2_avg_raw as (
    select 
    driver_id,
    avg(distance_km / fuel_consumed) as second_half_avg
    from trips
    where trip_date between date '2023-07-01' and last_day('2023-12-01')
    group by 1
)
select 
a.driver_id,
c.driver_name,
round(b.first_half_avg, 2) as first_half_avg,
round(a.second_half_avg, 2) as second_half_avg,
round(a.second_half_avg - b.first_half_avg, 2) as efficiency_improvement
from h2_avg_raw a
inner join h1_avg_raw b on a.driver_id = b.driver_id
left join drivers c on a.driver_id = c.driver_id
where (a.second_half_avg - b.first_half_avg) > 0
order by efficiency_improvement desc, driver_name asc


