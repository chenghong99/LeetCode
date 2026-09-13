WITH temp AS (SELECT 
managerId
FROM Employee
GROUP BY 1
HAVING COUNT(id) >= 5)
SELECT
name 
FROM temp INNER JOIN Employee
ON temp.managerId = Employee.id