-- https://leetcode.com/problems/biggest-single-number
SELECT 
MAX(num) AS num
FROM (
    SELECT
    num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
)