-- Script: 11-best_score.sql
-- Task: List all records with a score >= 10 in the table second_table from the database hbtn_0c_0.

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will list all records with a score >= 10 from the table second_table.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
