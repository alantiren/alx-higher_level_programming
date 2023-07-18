-- Script: 100-move_to_utf8.sql
-- Task: Convert hbtn_0c_0 database, first_table table, and name field to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).

-- Replace 'your_database_name' with the name of the database.
USE your_database_name;

-- This SQL query will convert the hbtn_0c_0 database to UTF8.
ALTER DATABASE your_database_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- This SQL query will convert the first_table table to UTF8.
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- This SQL query will convert the name field in first_table to UTF8.
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
