# Write your MySQL query statement below
## Find first order and check if date is the same
WITH raw AS (
    SELECT 
    delivery_id,
    customer_id,
    order_date,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rnk,
    customer_pref_delivery_date
    FROM Delivery
)

SELECT
ROUND(
    COUNT(DISTINCT customer_id)
    / (SELECT COUNT(DISTINCT customer_id) FROM Delivery)
    * 100
, 2) AS immediate_percentage
FROM raw
WHERE rnk = 1
AND order_date = customer_pref_delivery_date