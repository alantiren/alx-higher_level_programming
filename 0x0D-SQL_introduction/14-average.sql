-- Script: 14-average.sql
-- Task: Compute the score average of all records in the table second_table from the database hbtn_0c_0.

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will compute the score average of all records in the table second_table.
SELECT AVG(score) AS average FROM second_table;
