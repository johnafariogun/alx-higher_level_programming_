-- Lists all cities in the database hbtn_0d_usa sorting in ascending cities id order
SELECT city.`id`, city.`name`, state.`name` FROM `cities` AS city INNER JOIN `states` AS state ON city.`state_id` = state.`id` ORDER BY city.`id`;
