DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    owner_name VARCHAR(255)
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    species VARCHAR(255),
    name VARCHAR(255),
    owner_id INT REFERENCES owners(id)
);