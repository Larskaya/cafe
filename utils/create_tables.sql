CREATE TABLE IF NOT EXISTS storages_names (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS storages (
    id SERIAL PRIMARY KEY,
    capacity INT NOT NULL,
    designation INT REFERENCES storages_names(id)
);

CREATE TABLE IF NOT EXISTS cook_actions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    received_at TIMESTAMP DEFAULT Now()
);

CREATE TABLE IF NOT EXISTS products_in_storages (
    product_id INT REFERENCES products(id),
    storage_id INT REFERENCES storages(id)
);

CREATE TABLE IF NOT EXISTS ovens (
    id SERIAL PRIMARY KEY,
    working SMALLINT NOT NULL
);

CREATE TABLE IF NOT EXISTS bakers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS recipes_names (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    recipe SMALLINT REFERENCES recipes_names(id),
    need_to_cook SMALLINT NOT NULL,
    cook_action INT REFERENCES cook_actions(id)
);

CREATE TABLE IF NOT EXISTS recipes (
    id SERIAL PRIMARY KEY,
    recipe INT REFERENCES recipes_names(id),
    ingredient INT REFERENCES ingredients(id)
);