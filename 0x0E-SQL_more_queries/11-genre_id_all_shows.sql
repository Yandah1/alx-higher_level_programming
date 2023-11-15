-- lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_show.title, tv_genre.genre_id FROM tv_shows tv_show
LEFT JOIN tv_show_genres tv_show_genre
ON tv_genre.show_id = tv_show.id OR tv_genre.show_id = NULL
ORDER BY tv_show.title, tv_show_genre.genre_id ASC;
