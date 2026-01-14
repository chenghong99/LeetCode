# Write your MySQL query statement below
# first cte group by student having count(courseId) >= 5 and rating >= 4
# join on user id to have 2 x course name wher clause for compeletion date a < b 
# group by the 2 courses and count
with raw_user as (
    select 
    user_id,
    count(distinct course_id),
    avg(course_rating) 
    from course_completions
    group by 1
    having count(distinct course_id) >= 5
    and avg(course_rating) >= 4
), course_pair as (
    select 
    a.user_id, 
    course_name,
    LEAD(course_name) OVER (PARTITION BY a.user_id ORDER BY completion_date) AS next_course
    from course_completions a
    inner join raw_user b on a.user_id = b.user_id
) 
select 
course_name as first_course,
next_course as second_course,
count(*) as transition_count
from 
course_pair
where next_course is not null
group by 1,2
order by 3 desc, 1, 2