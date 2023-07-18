-- Script: 101-avg_temperatures.sql
-- Task: Display the average temperature (Fahrenheit) by city ordered by temperature (descending).
-- This SQL query will calculate the average temperature (Fahrenheit) by city and order the result by temperature (descending).
SELECT city, AVG(temperature) AS avg_temp FROM weather GROUP BY city ORDER BY avg_temp DESC;
