-- 5-unique_id.sql

-- Create the table unique_id if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1,
  name VARCHAR(256),
  UNIQUE (id)
);
