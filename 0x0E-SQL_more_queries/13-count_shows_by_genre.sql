-- 13-count_shows_by_genre.sql

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List all genres and the number of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;