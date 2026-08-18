# Write your MySQL query statement below
## min postiive test date, min negative test date > min postiive test date

WITH min_positive_cte AS (
    SELECT 
        patient_id,
        MIN(test_date) AS min_positive
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
),
min_negative_cte AS (
    SELECT 
        t.patient_id,
        MIN(t.test_date) AS min_negative
    FROM covid_tests t
    JOIN min_positive_cte p ON t.patient_id = p.patient_id
    WHERE t.result = 'Negative' 
      AND t.test_date > p.min_positive
    GROUP BY t.patient_id
), raw AS (
SELECT 
    p.patient_id,
    patient_name, 
    age,
    DATEDIFF(min_negative, min_positive) AS recovery_time
FROM min_positive_cte p
LEFT JOIN min_negative_cte n ON p.patient_id = n.patient_id
LEFT JOIN patients pt ON p.patient_id = pt.patient_id
) 
SELECT * 
FROM raw 
WHERE recovery_time IS NOT NULL
ORDER BY 4, 2
