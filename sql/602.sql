-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends
WITH t1 AS (
    SELECT
        requester_id AS id,
        COUNT(accepter_id) AS num
    FROM RequestAccepted
    GROUP BY requester_id
    UNION ALL
    SELECT
        accepter_id AS id,
        COUNT(requester_id) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
)
SELECT
    id,
    SUM(num) AS num
FROM t1
GROUP BY id
ORDER BY num DESC
LIMIT 1