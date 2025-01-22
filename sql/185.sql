-- https://leetcode.com/problems/department-top-three-salaries
with t1 as (
    select
        id,
        name,
        salary,
        departmentId,
        dense_rank() over (partition by departmentId order by salary desc) as salary_rank
    from Employee
)
select
    d.name as Department,
    t1.name as Employee,
    t1.salary as Salary
from t1
join Department d
on t1.departmentId=d.id
where t1.salary_rank <=3