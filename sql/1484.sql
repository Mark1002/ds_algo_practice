-- https://leetcode.com/problems/group-sold-products-by-the-date
select
    sell_date,
    count(distinct product) as num_sold,
    STRING_AGG(distinct product, ',' order by product) as products  
from Activities
group by sell_date
order by sell_date