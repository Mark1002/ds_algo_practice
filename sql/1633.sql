-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/
select
    contest_id,
    round(count(user_id)/(select count(*) from Users)::numeric*100, 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id asc
