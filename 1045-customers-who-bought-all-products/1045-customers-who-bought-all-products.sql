# Write your MySQL query statement below


# SELECT customer_id 
# FROM Customer 
# GROUP BY customer_id 
# HAVING COUNT(DISTINCT product_key) = SELECT COUNT DISTINCT product_key FROM Product 


SELECT customer_id
FROM   customer
GROUP  BY customer_id
HAVING Count(DISTINCT product_key) = (SELECT
       Count(DISTINCT product_key) FROM   product) 