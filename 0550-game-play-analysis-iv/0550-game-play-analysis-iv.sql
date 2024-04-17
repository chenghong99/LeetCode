# Write your MySQL query statement below

##count number of distinict player 
## group by pyaer and get min start date 
## select date where the start date is 1 day less 

SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT a1.player_id)
FROM Activity a1) , 2) AS fraction  
FROM Activity a2
WHERE (a2.player_id, DATE_SUB(a2.event_date, INTERVAL 1 DAY)) IN
(SELECT a3.player_id, MIN(a3.event_date)
FROM Activity a3
GROUP BY a3.player_id)

