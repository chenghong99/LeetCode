# Write your MySQL query statement below

## group by product id 
## select the min year 

SELECT s1.product_id, s1.year AS first_year, s1.quantity, s1.price
FROM Sales s1
WHERE (s1.product_id, s1.year) IN 
(SELECT s2.product_id, MIN(s2.year)
FROM Sales s2
GROUP BY s2.product_id) 
