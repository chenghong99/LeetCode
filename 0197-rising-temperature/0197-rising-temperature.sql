# Write your MySQL query statement below
WITH temp AS (SELECT 
w2.id, 
w1.temperature AS w1_temp,
w2.temperature AS w2_temp
FROM Weather w1
INNER JOIN Weather w2 ON w1.recordDate = DATE_SUB(w2.recordDate, INTERVAL 1 DAY)
) 
SELECT id FROM temp
WHERE w1_temp < w2_temp