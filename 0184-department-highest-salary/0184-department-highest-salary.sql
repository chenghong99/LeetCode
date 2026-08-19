# Write your MySQL query statement below
# dense rank partiton by departmentId order by salary -> return all rank 1

WITH ranking AS (
    SELECT id,
    name,
    salary, 
    departmentId,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
) 
SELECT 
d.name AS Department,
r.name AS Employee,
salary
FROM ranking r
INNER JOIN Department d ON r.departmentId = d.id
WHERE salary_rank = 1