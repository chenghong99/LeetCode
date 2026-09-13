# Write your MySQL query statement below
## CTE for valid dates min date + 7 onwards 
WITH valid_dates AS (
    SELECT DISTINCT c.visited_on
    FROM Customer c
    WHERE c.visited_on >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
)
SELECT 
d.visited_on,
SUM(CASE WHEN c.visited_on BETWEEN DATE_SUB(d.visited_on, INTERVAL 6 DAY) AND d.visited_on THEN amount END) AS amount,
ROUND(SUM(c.amount) / 7, 2) AS average_amount
FROM Customer c
INNER JOIN valid_dates d ON c.visited_on BETWEEN DATE_SUB(d.visited_on, INTERVAL 6 DAY) AND d.visited_on
GROUP BY 1
ORDER BY 1;