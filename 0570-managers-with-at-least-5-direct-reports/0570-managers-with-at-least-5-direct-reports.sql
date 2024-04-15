# Write your MySQL query statement below

## under manager id more than 5 ppl 
## get the manager id of those with more than 5 and match with employee table

SELECT e2.name
FROM Employee e2
WHERE e2.id IN 
(SELECT e1.managerId 
FROM Employee e1
GROUP BY e1.managerId 
HAVING COUNT(e1.managerId) >= 5)
