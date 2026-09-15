# Write your MySQL query statement below
## fitler bookid coun session id
WITH raw AS (
    SELECT
    book_id
    ,MAX(session_rating) AS highest_rating
    ,MIN(session_rating) AS lowest_rating
    ,SUM(CASE WHEN session_rating >= 4 THEN 1 END) AS high_rating_count
    ,SUM(CASE WHEN session_rating <= 2 THEN 1 END) AS low_rating_count
    ,SUM(CASE WHEN session_rating >= 4 THEN 1 
    WHEN session_rating <= 2 THEN 1 END) / COUNT(session_id) AS polarization_score
    FROM reading_sessions
    GROUP BY 1
    HAVING COUNT(session_id) >= 5
    AND high_rating_count >= 1
    AND low_rating_count >= 1
)
SELECT 
r.book_id,
title,
author,
genre,
pages,
highest_rating - lowest_rating AS rating_spread,
ROUND(polarization_score, 2) AS polarization_score
FROM raw r
INNER JOIN books b ON
r.book_id = b.book_id
WHERE polarization_score >= 0.6
ORDER BY polarization_score DESC, title DESC