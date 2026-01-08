# Write your MySQL query statement below
## inner join tiv_2015 to get all pid with same tiv_2015 
## group by lat and lon and count * == 0

with unique_lat_lon as (
    select
    lat, 
    lon, 
    count(*) row_count
    from Insurance
    group by 1, 2
    having count(*) = 1
), dup_tiv_2015 as (
    select 
    tiv_2015
    ,count(*) as dup_count
    from Insurance
    group by 1
    having count(*) > 1
)
select 
round(sum(tiv_2016), 2) as tiv_2016
from Insurance a 
inner join dup_tiv_2015 b on 
a.tiv_2015 = b.tiv_2015
inner join unique_lat_lon c on 
a.lat = c.lat and
a.lon = c.lon