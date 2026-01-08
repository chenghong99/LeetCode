# Write your MySQL query statement below
with manager_id as (
    select 
    managerId,
    count(*) as manager_count
    from Employee
    group by 1
    having count(*) >= 5) 
    
    select name
    from Employee a
    inner join manager_id b on a.id = b.managerId