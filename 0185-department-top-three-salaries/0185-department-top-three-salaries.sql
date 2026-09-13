# Write your MySQL query statement below
## use dense rank tie even


WITH emp_rnk AS (
    SELECT 
    e.id,
    e.name AS Employee,
    d.name AS Department,
    salary AS Salary,
    departmentId,
    DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) as rnk
    FROM Employee e
    LEFT JOIN Department d ON e.departmentId = d.id
) 
SELECT 
Department,
Employee,
Salary
FROM emp_rnk
WHERE rnk <= 3