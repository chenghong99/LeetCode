WITH raw AS (
    SELECT
    managerId
    FROM Employee
    GROUP BY 1
    HAVING COUNT(id) >= 5)

SELECT name from raw INNER JOIN Employee on raw.managerId = Employee.id