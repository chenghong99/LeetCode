# Write your MySQL query statement below
# Write your MySQL query statement below
## gaps and island. row number order by num - id  should be the same
WITH raw AS (
    SELECT 
    id, 
    num,
    ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS row_num
    FROM Logs
), temp AS (
    SELECT 
    num,
    id - row_num AS island
    FROM raw
) 
SELECT DISTINCT num AS ConsecutiveNums FROM temp
GROUP BY num, island
HAVING COUNT(*) >= 3