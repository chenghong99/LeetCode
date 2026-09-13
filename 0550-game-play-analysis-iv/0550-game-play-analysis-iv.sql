# Write your MySQL query statement below
WITH min_date AS (
    SELECT 
    player_id,
    MIN(event_date) AS first_login
    FROM Activity
    GROUP BY 1
)
SELECT 
ROUND(COUNT(DISTINCT a.player_id)/ (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity a
INNER JOIN min_date m 
ON a.player_id = m.player_id 
AND a.event_date = DATE_ADD(m.first_login, INTERVAL 1 DAY)