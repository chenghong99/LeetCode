# Write your MySQL query statement below


SELECT e1.reports_to AS employee_id, (
    SELECT 
      name 
    FROM 
      employees e 
    WHERE 
      e1.reports_to = e.employee_id 
  ) AS name, COUNT(*) AS reports_count, ROUND(SUM(e1.age)/COUNT(*)) AS average_age 
FROM Employees e1
WHERE e1.reports_to IS NOT NULL
GROUP BY e1.reports_to 
HAVING COUNT(*) >= 1
ORDER BY employee_id
