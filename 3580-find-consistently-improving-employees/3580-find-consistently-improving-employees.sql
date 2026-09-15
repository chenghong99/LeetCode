# Write your MySQL query statement below
## fitler at least 3 review, 
## join the filter and rank reviews date

WITH raw AS (
    SELECT 
    employee_id,
    rating,
    ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) review_order
    FROM performance_reviews
), temp AS (
    SELECT 
    employee_id,
    MAX(CASE WHEN review_order = 1 THEN rating END) AS latest,
    MAX(CASE WHEN review_order = 2 THEN rating END) AS middle,
    MAX(CASE WHEN review_order = 3 THEN rating END) AS first
    FROM raw
    WHERE review_order <= 3
    GROUP BY 1
    HAVING COUNT(*) >= 3
) 
SELECT 
t.employee_id
,name
,latest - first AS improvement_score
FROM temp t
LEFT JOIN employees e
ON t.employee_id = e.employee_id
WHERE latest > middle
AND middle > first
ORDER BY 3 DESC, 2 ASC;