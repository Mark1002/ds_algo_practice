-- https://leetcode.com/problems/patients-with-a-condition/
with t1 as (
    SELECT
        patient_id,
        patient_name,
        conditions,
        unnest(STRING_TO_ARRAY(conditions, ' ')) as disease
    FROM Patients
)
select
    DISTINCT
    patient_id,
    patient_name,
    conditions
from t1
WHERE disease like 'DIAB1%'