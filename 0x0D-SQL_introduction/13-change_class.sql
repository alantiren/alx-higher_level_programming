-- Script: 13-change_class.sql
-- Task: Remove all records with a score <= 5 in the table second_table from the database hbtn_0c_0.
-- This SQL query will remove all records with a score <= 5 from the table second_table.
DELETE FROM second_table WHERE score <= 5;
