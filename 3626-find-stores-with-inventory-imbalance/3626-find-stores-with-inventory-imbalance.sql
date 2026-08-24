WITH process_1 AS (
    SELECT  
    a.store_id,
    store_name,
    location,
    MAX(price) AS max_price,
    MIN(price) as min_price
    FROM inventory a
    LEFT JOIN stores b ON a.store_id = b.store_id
    GROUP BY 1,2,3
    HAVING COUNT(*) >= 3
), process_2 AS (
    SELECT 
    a.store_id,
    store_name,
    location,
    product_name,
    quantity,
    price
    FROM inventory a 
    INNER JOIN process_1 b ON a.store_id = b.store_id AND (a.price = max_price OR a.price = min_price)
) 
SELECT
a.store_id, a.store_name, a.location, a.product_name AS most_exp_product, 
b.product_name AS cheapest_product, round( b.quantity / a.quantity , 2) imbalance_ratio  
FROM process_2 a 
INNER JOIN process_2 b ON a.store_id = b.store_id AND a.price > b.price AND a.quantity < b.quantity
ORDER BY imbalance_ratio DESC, store_name