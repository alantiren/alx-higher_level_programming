-- Script: 12-no_cheating.sql
-- Task: Update the score of Bob to 10 in the table second_table.

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will update the score of Bob to 10 based on his name.
UPDATE second_table SET score = 10 WHERE name = 'Bob';
