-- My genres
-- uses the hbtn_0d_tvshows database to lists all genres of the show Comedy
SELECT g.title
FROM tv_shows AS g
INNER JOIN tv_show_genres AS s
ON g.id = s.show_id
INNER JOIN tv_genres AS t
ON t.id = s.genre_id
WHERE t.name = "Comedy"
ORDER BY g.title ASC;
