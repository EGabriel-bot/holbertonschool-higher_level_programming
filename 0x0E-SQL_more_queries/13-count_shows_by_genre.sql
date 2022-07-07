-- No genre
-- lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT g.genre, s.number_of_shows
FROM tv_genres AS g
LEFT JOIN tv_show_genres AS s
ON g.name = s.show_id
WHERE s.show_id IS NOT NULL
ORDER BY s.number_of_shows DESC;
