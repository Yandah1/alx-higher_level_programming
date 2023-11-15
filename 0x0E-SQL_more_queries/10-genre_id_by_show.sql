--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows tvs
INNER JOIN tv_show_genres tv_show_genre
ON tv_show_genre.show_id = tv_show.id
ORDER BY tv_show.title, tv_genre.genre_id ASC;