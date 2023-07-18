-- Script: 16-no_link.sql
-- Task: List all records of the table second_table from the database hbtn_0c_0.
-- This SQL query will list all records of the table second_table, excluding rows without a name value, and order them by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
