-- lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows tvs
LEFT JOIN tv_show_genres tv_show_genres
ON tv_genres.show_id = tv_show.id OR tv_genres.show_id = NULL
ORDER BY tv_show.title, tv_show_genres.genre_id ASC;
