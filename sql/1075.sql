-- https://leetcode.com/problems/project-employees-i
SELECT
    project_id,
    round(avg(experience_years), 2) as average_years
FROM Project p
JOIN Employee e
USING (employee_id)
GROUP BY project_id