# Write your MySQL query statement below
SELECT e1.name  
FROM Employee e1
WHERE e1.id IN 
(SELECT e2.managerId  
FROM Employee e2 
WHERE e2.managerId IS NOT NULL 
GROUP BY e2.managerId 
HAVING COUNT(*) >= 5)