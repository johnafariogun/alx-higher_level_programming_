-- Displays the average temperatures in fahrenheight orderred by descending temperatures in temperatures.sql
SELECT `city`, AVG(`value`) AS `avg_temp` FROM `temperatures` GROUP BY `city` ORDER BY `avg_temp` DESC;
