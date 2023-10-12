CREATE TABLE todo (
    id serial PRIMARY KEY,
    title VARCHAR (100) NOT NULL,
    completed BOOLEAN DEFAULT false
);

