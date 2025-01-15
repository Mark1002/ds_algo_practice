-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/
SELECT
    product_name,
    sum(o.unit) AS unit
FROM Products p
JOIN Orders o USING(product_id)
where order_date > '2020-01-31'
and order_date < '2020-03-01'
group by product_name
having sum(o.unit) >= 100