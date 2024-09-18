-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports
WITH T AS (
    SELECT
    managerId 
    FROM Employee
    WHERE managerId is not null
    GROUP BY managerId
    HAVING count(1) >= 5
)
SELECT E.name
FROM Employee AS E
JOIN T
ON E.id = T.managerId
