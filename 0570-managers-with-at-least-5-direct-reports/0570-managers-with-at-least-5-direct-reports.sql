# Write your MySQL query statement below

SELECT e2.name
FROM Employee e2
JOIN (SELECT e1.managerId, COUNT(*) AS staff_count
FROM Employee e1
WHERE e1.managerId IS NOT NULL
GROUP BY e1.managerId) e3 ON e2.id = e3.managerId
WHERE e3.staff_count >= 5

