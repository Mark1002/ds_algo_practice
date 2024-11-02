-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee
SELECT
    t2.employee_id,
    t2.name,
    count(t1.employee_id) as reports_count,
    round(avg(t1.age)) as average_age
FROM Employees as t1
join Employees as t2
on t1.reports_to = t2.employee_id
group by t2.employee_id, t2.name
order by t2.employee_id