-- No genre
-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON g.id = s.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
