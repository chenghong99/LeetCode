# Write your MySQL query statement below

SELECT MAX(f.num) AS num 
FROM (SELECT n.num
FROM MyNumbers n
GROUP BY n.num
HAVING COUNT(*) = 1) f