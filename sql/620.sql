-- https://leetcode.com/problems/not-boring-movies
SELECT * FROM Cinema
WHERE mod(id, 2) <> 0
AND description <> 'boring'
ORDER BY rating DESC