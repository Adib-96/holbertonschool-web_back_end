-- This SQL script creates a 'users' table with specific attributes.
-- The script includes checks to ensure it does not fail if the table already exists.

CREATE TABLE IF NOT EXISTS users (
    -- 'id' is an integer that auto-increments and serves as the primary key.
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- 'email' is a string with a maximum length of 255 characters.
    -- It is required and must be unique for each user.
    email VARCHAR(255) NOT NULL UNIQUE,
    
    -- 'name' is a string with a maximum length of 255 characters.
    -- It is optional and can be null.
    name VARCHAR(255),
    
    -- 'country' is an enumeration type with values 'US', 'CO', and 'TN'.
    -- It is required and defaults to 'US' if no value is provided.
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
