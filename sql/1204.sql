-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/
SELECT
    person_name
FROM
(
    SELECT
    person_name,
    SUM(weight) over (order by turn) AS acc_weight
    FROM Queue
)
WHERE acc_weight <= 1000
ORDER BY acc_weight DESC limit 1