"""https://leetcode.com/problems/second-highest-salary."""
-- Better approach
SELECT max(Salary) as "SecondHighestSalary"
    FROM Employee
WHERE Salary < (SELECT max(Salary) FROM Employee)
-- My approach
WITH t1 AS (
    SELECT
        id,
        salary,
        dense_rank() over(order by salary desc) as rank
    FROM Employee
)
SELECT
    case
        when COUNT(id)=1 then null
        else (SELECT distinct salary from t1 where rank=2)
    end as "SecondHighestSalary"
FROM t1