-- Lag Window Function Solution
with temp as (
    select
        num,
        lag(num, 1) over () as prev_1,
        lag(num, 2) over () as prev_2
    from logs
)
select distinct num as ConsecutiveNums
from temp where num = prev_1 and num = prev_2

-- Self Join Solution
select
    distinct l1.num as ConsecutiveNums
from logs as l1
join logs as l2 on l1.id=l2.id+1
join logs as l3 on l2.id=l3.id+1
and l1.num=l2.num and l2.num=l3.num