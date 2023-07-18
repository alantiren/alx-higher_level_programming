-- Script: 7-insert_value.sql
-- Task: Insert a new row in the table first_table in the hbtn_0c_0 database.
-- Insert a new row with id=89 and name="Best School". The IGNORE keyword ensures that the row won't be inserted if it already exists.
INSERT IGNORE INTO first_table (id, name) VALUES (89, "Best School");
