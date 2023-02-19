-- Lists all cities of California in the database hbtn_0d_usa ordered by acscending order id
SELECT `id`, `name` FROM `cities` WHere `state_id` IN (
	SELECT `id` FROM `states` WHERE `name` = "California")
	ORDER BY `id`;
