NOT EXISTS CREATE TABLE fridges (
    id SERIAL PRIMARY KEY,
);

NOT EXISTS CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    received_at TIMESTAMP DEFAULT Now()
    CONSTRAINT fk_fridge FOREIGN KEY(fridge_id) REFERENCES fridges(id),
);