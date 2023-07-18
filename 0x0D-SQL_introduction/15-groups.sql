-- Script: 15-groups.sql
-- Task: List the number of records with the same score in the table second_table from the database hbtn_0c_0.

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will list the number of records with the same score and sort the list by the number of records in descending order.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
