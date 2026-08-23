WITH pre_aggr AS (
    SELECT 
    person_id,
    person_name,
    SUM(weight) OVER (ORDER BY turn) AS cum_sum
    FROM Queue
) SELECT person_name FROM pre_aggr WHERE cum_sum <= 1000 ORDER BY cum_sum DESC limit 1