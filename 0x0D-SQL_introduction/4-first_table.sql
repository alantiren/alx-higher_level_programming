-- Script: 4-first_table.sql
-- Task: Create a table called first_table in the current database of your MySQL server.
-- This SQL query will create the table first_table if it doesn't exist.
CREATE TABLE IF NOT EXISTS `first_table` (`id` INT, `name` VARCHAR(256));