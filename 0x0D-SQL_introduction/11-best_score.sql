-- Lists all records in second_table with score >= 10 ordered by scores in descendng order
iSELECT `score`, `name` FROM `second_table` WHERE `score` >= 10 ORDER BY `score` DESC;
