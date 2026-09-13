# Write your MySQL query statement below
## use double lead 
WITH temp AS (
    SELECT 
    id, 
    num,
    LEAD(num) OVER (ORDER BY id) AS next_num,
    LEAD(num, 2) OVER (ORDER BY id) AS next_next_num
    FROM Logs 
) 
SELECT 
DISTINCT num AS ConsecutiveNums
FROM temp t1
WHERE (num = next_num) AND (num = next_next_num)