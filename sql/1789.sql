-- https://leetcode.com/problems/primary-department-for-each-employee
SELECT
employee_id,
COALESCE(
    MAX(department_id) FILTER (WHERE primary_flag='Y'),
    MAX(department_id)
) AS department_id
FROM Employee
GROUP BY employee_id