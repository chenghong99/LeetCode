WITH temp AS (
    SELECT 
    person_id,
    person_name,
    weight,
    turn,
    SUM(weight) OVER (ORDER BY turn) AS cum_sum
    FROM Queue
) 
SELECT 
person_name
FROM temp
WHERE cum_sum <= 1000 
ORDER BY cum_sum DESC
LIMIT 1