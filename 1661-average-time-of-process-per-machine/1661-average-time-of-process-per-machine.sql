# Write your MySQL query statement below


## group by machine id then process id sum all the end - sum all the start then divide by num 

SELECT machine_id, 
ROUND(SUM(CASE WHEN activity_type = 'end' THEN timestamp ELSE (-1 * timestamp) END) / (COUNT(*)/2), 3) AS processing_time 
FROM Activity 
GROUP BY machine_id