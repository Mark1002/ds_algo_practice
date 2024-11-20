-- https://leetcode.com/problems/count-salary-categories
WITH t1 AS (
    SELECT
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            WHEN income > 50000 THEN 'High Salary'
        END AS category,
        COUNT(account_id) AS accounts_count
    FROM Accounts
    GROUP BY category
),
t2 AS (
    SELECT 'Low Salary' AS category, 0 AS accounts_count
    UNION
    SELECT 'Average Salary' AS category, 0 AS accounts_count
    UNION
    SELECT 'High Salary' AS category, 0 AS accounts_count
)
SELECT
    t2.category,
    COALESCE(t1.accounts_count, t2.accounts_count) AS accounts_count
FROM t2
LEFT JOIN t1
ON t2.category = t1.category