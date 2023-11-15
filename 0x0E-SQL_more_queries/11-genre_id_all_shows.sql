-- lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON tv_genres.show_id = tv_show.id
ORDER BY tv_show.title, tv_show_genres.genre_id ASC;
