# Write your MySQL query statement below


## count total rows for table using select count(*) table
## group by contest id and count rows / by total 

SELECT r.contest_id, 
ROUND((COUNT(*))/ (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM Register r 
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC

