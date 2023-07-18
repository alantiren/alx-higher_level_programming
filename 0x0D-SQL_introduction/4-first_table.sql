-- Script: 4-first_table.sql
-- Task: Create a table called first_table in the current database of your MySQL server.

-- Replace 'your_database_name' with the name of the current database.
USE your_database_name;

-- This SQL query will create the table first_table if it doesn't exist.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
