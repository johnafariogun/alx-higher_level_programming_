-- Lists all records in second_table with the same name orderred by score
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
