-- Script: 103-max_state.sql
-- Task: Display the maximum temperature of each state, ordered by state name.
-- This SQL query will calculate the maximum temperature for each state and order the result by state name.
SELECT state, MAX(temperature) AS max_temp
FROM weather
GROUP BY state
ORDER BY state;
