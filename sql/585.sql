-- https://leetcode.com/problems/investments-in-2016
WITH t1 AS (
    SELECT
        tiv_2016,
        COUNT(1) OVER(PARTITION BY tiv_2015) AS tiv_2015_count,
        COUNT(1) OVER(PARTITION BY lat, lon) AS latlon_count
    FROM
    Insurance
)
SELECT
    round(cast(SUM(tiv_2016) as NUMERIC), 2) AS tiv_2016
FROM t1
WHERE latlon_count=1 AND tiv_2015_count > 1