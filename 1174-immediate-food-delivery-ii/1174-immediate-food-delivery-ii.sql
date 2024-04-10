# Write your MySQL query statement below

SELECT ROUND((SUM(CASE WHEN f.order_date = f.customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*))*100, 2) AS immediate_percentage 
FROM (SELECT d.customer_id, MIN(d.order_date) AS order_date, MIN(d.customer_pref_delivery_date) AS customer_pref_delivery_date 
FROM Delivery d
GROUP BY d.customer_id) f

## get th first order so group by cust id and order by date and return first 
## compare using case when first date = pref date

