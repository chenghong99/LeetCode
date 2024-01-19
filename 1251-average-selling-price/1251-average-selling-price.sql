# Write your MySQL query statement below
select p.product_id, COALESCE(round(sum(price*units)/sum(units),2), 0) as average_price 
from prices p

LEFT JOIN 
UnitsSold u
ON 

p.product_id = u.product_id AND 
u.purchase_date BETWEEN p.start_date AND p.end_date
group by product_id;