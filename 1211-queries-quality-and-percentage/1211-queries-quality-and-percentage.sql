# Write your MySQL query statement below
WITH raw AS (
    SELECT 
    query_name,
    result,
    position,
    rating,
    rating/position AS quality
    FROM Queries
)
SELECT 
query_name,
ROUND(AVG(quality), 2) AS quality,
COALESCE(ROUND((SUM(CASE WHEN rating < 3 THEN 1 END)/COUNT(position))*100,2), 0) AS poor_query_percentage
FROM raw
GROUP BY 1