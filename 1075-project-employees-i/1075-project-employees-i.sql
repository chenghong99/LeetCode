# Write your MySQL query statement below
SELECT p.project_id, ROUND(SUM(e.experience_years)/COUNT(p.employee_id), 2) AS average_years 
FROM Project p 
INNER JOIN Employee e ON p.employee_id = e.employee_id
WHERE e.experience_years IS NOT NULL
GROUP BY project_id
