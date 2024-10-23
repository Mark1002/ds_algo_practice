-- https://leetcode.com/problems/product-price-at-a-given-date
WITH t1 AS (
    SELECT
    product_id, max(change_date) as new_date
    FROM products where change_date <= '2019-08-16'
    GROUP BY product_id
),
t2 AS (
    select
        p.product_id,
        p.new_price
    from products p
    join t1 on (
        p.product_id=t1.product_id
        and p.change_date=t1.new_date
    ) 
),
t3 AS(
    SELECT product_id FROM products GROUP BY product_id
)
SELECT
    product_id,
    COALESCE(new_price, 10) AS price
FROM t3 LEFT JOIN t2
USING (product_id)
ORDER BY product_id