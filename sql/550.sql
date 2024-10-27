-- https://leetcode.com/problems/game-play-analysis-iv
WITH t1 AS (
    SELECT
    player_id,
    event_date,
    lag(event_date) over (partition by player_id order by event_date) as pre_date,
    rank() over (partition by player_id order by event_date) as rk
    FROM Activity
),
t2 AS (
    select
        player_id,
        rk,
        case when event_date-1=pre_date then 1 else 0 end as is_consec
    from t1
)
select
    round(
        count(player_id) filter (where is_consec=1 and rk=2)*1.0/count(distinct player_id),
        2
    ) as fraction
from t2