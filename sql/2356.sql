-- https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher
SELECT
    teacher_id,
    count(distinct subject_id) as cnt
FROM Teacher
GROUP BY teacher_id