-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier
SELECT
t2.unique_id,
t1.name
FROM Employees AS t1
LEFT JOIN EmployeeUNI AS t2
USING (id)