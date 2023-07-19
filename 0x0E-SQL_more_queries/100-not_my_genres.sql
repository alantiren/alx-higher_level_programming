-- 100-not_my_genres.sql

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Get the genre ID for the show "Dexter"
SET @dexter_genre_id := (SELECT genre_id FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter' LIMIT 1);

-- List all genres not linked to the show "Dexter"
SELECT name
FROM tv_genres
WHERE id != @dexter_genre_id
ORDER BY name ASC;
