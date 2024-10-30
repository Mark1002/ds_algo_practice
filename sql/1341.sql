-- https://leetcode.com/problems/movie-rating
(
    select t2.name as results
    from MovieRating t1 join Users t2 using(user_id)
    group by t2.name
    ORDER BY count(t1.movie_id) desc, T2.name asc
    limit 1
)
UNION ALL
(
    select m2.title as results
    from MovieRating m1 join Movies m2 using(movie_id)
    where created_at >= '2020-02-01' and created_at < '2020-03-01'
    group by m2.title
    order by avg(rating) desc, m2.title asc
    limit 1
)