-- Lists all records with the same score in second_table orderred by number in descending order
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC
