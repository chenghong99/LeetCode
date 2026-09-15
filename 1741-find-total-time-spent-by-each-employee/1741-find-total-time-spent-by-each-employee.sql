# Write your MySQL query statement below
WITH raw AS (
    SELECT 
    emp_id,
    event_day,
    SUM(in_time) AS in_time,
    SUM(out_time) AS out_time
    FROM Employees
    GROUP BY 1, 2
)
SELECT 
event_day AS day,
emp_id,
out_time - in_time AS total_time
FROM raw