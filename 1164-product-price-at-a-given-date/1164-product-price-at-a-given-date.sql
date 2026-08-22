# Write your MySQL query statement below
## filter change_date less than 2019-08-16 group by product_id find max date and return rice 

WITH raw AS (
    SELECT 
    product_id
    ,new_price
    ,change_date
    ,ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) as row_num
    FROM Products
    WHERE change_date <= '2019-08-16'
), all_prod AS (
    SELECT DISTINCT product_id FROM Products
)
 SELECT a.product_id, 
 COALESCE(b.new_price, 10) AS  price
 FROM all_prod a
 LEFT JOIN raw b ON a.product_id = b.product_id
AND b.row_num = 1