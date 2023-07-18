-- Script: 11-best_score.sql
-- Task: List all records with a score >= 10 in the table second_table from the database hbtn_0c_0.
-- This SQL query will list all records with a score >= 10 from the table second_table.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
