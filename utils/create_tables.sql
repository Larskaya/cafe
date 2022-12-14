CREATE TABLE IF NOT EXISTS fridges (
    id SERIAL PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    received_at TIMESTAMP DEFAULT Now(),
    fridge_id INT REFERENCES fridges(id)
--    CONSTRAINT fk_fridge FOREIGN KEY(fridge_id) REFERENCES fridges(id)
);