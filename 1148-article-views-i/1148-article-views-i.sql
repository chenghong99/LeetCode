# Write your MySQL query statement below

## select cases where viewerid = author_id

SELECT DISTINCT author_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY author_id