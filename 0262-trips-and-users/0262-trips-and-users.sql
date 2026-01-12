# Write your MySQL query statement below
## first CTE, raw pool, date range ,unbanned 
## join first cte with second cte 

with raw_users as (
    select 
        users_id ## role 
    from Users
    where banned = 'No'
    and role in ('client', 'driver')
), raw_trips as (
    select
    id, 
    request_at,
    status
    from Trips a
    left join raw_users b on a.client_id = b.users_id
    left join raw_users c on a.driver_id = c.users_id
    where request_at between '2013-10-01' AND '2013-10-03' 
    and c.users_id is not null
    and b.users_id is not null
)
select 
request_at as 'Day', 
round(sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1
else 0 end)/ count(*), 2) as 'Cancellation Rate'
from raw_trips
group by 1
order by 1