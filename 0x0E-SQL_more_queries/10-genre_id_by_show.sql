-- lists all sbhows contained in hbtn_0d_tvshows nwhich have at least one genre linked sorted by ascending tvshows title and genre_id
SELECT serie.`title`, genre.`genre_id` FROM `tv_shows` AS serie INNER JOIN `tv_shows_genres` AS genre ON serie.`id` = genre.`show_id` ORDER BY serie.`title`, genre.`genre_id`;
