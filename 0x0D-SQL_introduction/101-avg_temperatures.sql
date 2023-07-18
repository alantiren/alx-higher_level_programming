-- Script: 101-avg_temperatures.sql
-- Task: Display the average temperature (Fahrenheit) by city ordered by temperature (descending).

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will calculate the average temperature (Fahrenheit) by city and order the result by temperature (descending).
SELECT city, AVG(temperature) AS avg_temp FROM weather GROUP BY city ORDER BY avg_temp DESC;
