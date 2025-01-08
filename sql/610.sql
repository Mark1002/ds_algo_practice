-- https://leetcode.com/problems/triangle-judgement
select
    x,
    y,
    z,
    case when 
    (x + z <= y or x + y <= z or z + y <= x) then 'No' else 'Yes'
    end as triangle
from Triangle