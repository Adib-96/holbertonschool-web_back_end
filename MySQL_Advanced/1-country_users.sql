-- This script creates a 'users' table in the database.
-- The table includes columns for user ID, email, name, and country.
-- The script will not fail if the table already exists due to the IF NOT EXISTS clause.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US','CO','TN') NOT NULL DEFAULT 'US',
);
