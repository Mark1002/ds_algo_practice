-- https://leetcode.com/problems/average-time-of-process-per-machine
WITH t1 as (
SELECT
    machine_id,
    process_id,
    activity_type,
    timestamp
FROM Activity
WHERE activity_type='start'
),
t2 as (
    SELECT
    machine_id,
    process_id,
    activity_type,
    timestamp
FROM Activity
WHERE activity_type='end'
),
t3 as (
    SELECT
        t1.machine_id,
        t1.process_id,
        (t2.timestamp - t1.timestamp) as process_time
    FROM t1 JOIN t2
    ON t1.machine_id = t2.machine_id and t1.process_id = t2.process_id
)
SELECT
    machine_id,
    ROUND(AVG(process_time)::numeric, 3) AS processing_time
FROM t3
GROUP BY machine_id