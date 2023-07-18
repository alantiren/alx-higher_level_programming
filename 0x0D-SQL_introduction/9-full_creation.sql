-- Script: 9-full_creation.sql
-- Task: Create a table called second_table in the database hbtn_0c_0 and add multiple rows.

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will create the table second_table if it doesn't exist.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- This SQL query will add the specified rows to the second_table.
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
