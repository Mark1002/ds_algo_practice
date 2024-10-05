-- https://leetcode.com/problems/exchange-seats
with t1 as (
    select
        id,
        student,
        case
            when mod(id, 2)=0 then id-1
            else id+1
        end as swap_id
    from Seat
)
select
    t2.id as id,
    COALESCE(t1.student, t2.student) as student
from Seat as t2
left join t1
on t2.id=t1.swap_id