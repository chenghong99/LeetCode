WITH temp AS (
    SELECT
    id, 
    num,
    ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS row_num
    FROM Logs
), raw AS (
SELECT 
num,
id - row_num AS island
FROM temp)
SELECT DISTINCT num AS ConsecutiveNums
FROM raw
GROUP BY num, island
HAVING COUNT(*) >= 3