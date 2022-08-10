-- script that uses the hbtn_0d_tvshows database to list all genres not
-- linked to the show Dexter.
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title
	FROM tv_shows
     	JOIN tv_show_genres
     	     ON tv_show_genres.show_id = tv_shows.id
     	JOIN tv_genres
     	     ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.id
) comedy_shows ON comedy_shows.title = tv_shows.title
WHERE comedy_shows.title is NULL
ORDER BY tv_shows.title;
