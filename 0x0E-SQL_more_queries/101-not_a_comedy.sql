-- 101-not_a_comedy.sql
-- Use the hbtn_0d_tvshows database
-- Get the genre ID for the genre "Comedy"
SET @comedy_genre_id := (SELECT id FROM tv_genres WHERE name = 'Comedy' LIMIT 1);

-- List all shows without the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
  SELECT show_id
  FROM tv_show_genres
  WHERE genre_id = @comedy_genre_id
)
ORDER BY tv_shows.title ASC;
