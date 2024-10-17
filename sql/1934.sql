-- https://leetcode.com/problems/confirmation-rate
WITH T1 AS (
    SELECT
        s.user_id as user_id,
        c.time_stamp as time_stamp,
        c.action as action,
        CASE 
        WHEN action='confirmed' THEN 1 ELSE 0 
        END AS action_count
    FROM Confirmations c
    FULL OUTER JOIN Signups s
    ON c.user_id=s.user_id
)
SELECT
    user_id,
    case
    when sum(action_count)=0 then 0
    else
    round(sum(action_count)*1.0 / count(time_stamp), 2)
    end AS confirmation_rate
FROM T1
group by
user_id