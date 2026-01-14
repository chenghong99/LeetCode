# Write your MySQL query statement below
with user_rating as (
    select 
    a.user_id,
    name,
    count(distinct movie_id) as num_movie
    from MovieRating a
    left join Users b on a.user_id = b.user_id
    group by 1, 2
    order by 3 desc, 2
    limit 1
), movie_rating as (
    select a.movie_id, 
    title,
    avg(rating)
    from MovieRating a
    left join Movies b on a.movie_id = b.movie_id
    where a.created_at between date '2020-02-01' and last_day(date '2020-02-01')
    group by 1, 2
    order by 3 desc, 2
    limit 1
)
select name as results from user_rating
union all select title as results from movie_rating