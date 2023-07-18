-- Script: 102-top_city.sql
-- Task: Display the top 3 cities' temperature during July and August ordered by temperature (descending).
-- This SQL query will calculate the average temperature (Fahrenheit) for each city during July and August, and order the result by temperature (descending).
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_temp` DESC
LIMIT 3;
