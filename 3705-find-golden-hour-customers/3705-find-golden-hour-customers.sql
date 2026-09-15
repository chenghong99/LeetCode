# Write your MySQL query statement below
## raw cte -> count total orders, peak hours orderm order rating, num or orders rated

    SELECT 
    customer_id,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(COUNT(CASE WHEN TIME_FORMAT(order_timestamp, '%H:%i') BETWEEN '11:00' AND '14:00' OR TIME_FORMAT(order_timestamp, '%H:%i') BETWEEN '18:00' AND '21:00' THEN 1 ELSE NULL END) / COUNT(order_id) * 100 , 0) peak_hour_percentage,
    ROUND(AVG(order_rating),2) average_rating 
    FROM restaurant_orders
    GROUP BY 1
    HAVING COUNT(order_id) >= 3 AND peak_hour_percentage >= 60
    AND average_rating >= 4.0 AND COUNT(order_rating) / COUNT(COALESCE(order_rating,1)) >= 0.5
    ORDER BY 4 DESC, 1 DESC