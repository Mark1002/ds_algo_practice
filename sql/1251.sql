-- https://leetcode.com/problems/average-selling-price
select
    p.product_id,
    coalesce(round(sum(u.units * p.price)*1.0/sum(u.units), 2), 0) as average_price
from Prices p
left join UnitsSold u
on (p.product_id = u.product_id
and u.purchase_date 
between p.start_date and p.end_date
)
group by p.product_id