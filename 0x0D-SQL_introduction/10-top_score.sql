-- Script: 10-top_score.sql
-- Task: List all records of the table second_table from the database hbtn_0c_0.

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will list all records of the table second_table.
SELECT score, name FROM second_table ORDER BY score DESC;
