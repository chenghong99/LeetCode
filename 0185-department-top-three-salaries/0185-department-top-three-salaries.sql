# Write your MySQL query statement below
with raw as (
    select 
    b.name as "Department",
    a.name as "Employee",
    salary as "Salary",
    DENSE_RANK()over(partition by b.name order by salary DESC) as rnk
    from Employee a 
    left join Department b on a.departmentId = b.id
) select Department, 
 Employee, Salary from raw where rnk <= 3