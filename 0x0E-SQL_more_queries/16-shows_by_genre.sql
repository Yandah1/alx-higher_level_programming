-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT tv_shows.title, genres.name
FROM tv_shows tvg
LEFT JOIN tv_show_genres tvg  ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres g ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, genres.name ASC;
