-- 9-cities_by_state_join.sql
-- List all cities with their respective state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
