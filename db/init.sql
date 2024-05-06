-- images table
CREATE TABLE images (
    image_id SERIAL PRIMARY KEY,
    image_name VARCHAR(255) UNIQUE NOT NULL,
    created_at: TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW())
);