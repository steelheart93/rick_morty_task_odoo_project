
-- Esquema básico para PostgreSQL
CREATE TABLE IF NOT EXISTS "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS task (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    due_date DATE,
    status VARCHAR(50),
    user_id INTEGER REFERENCES "user"(id),
    character_id INTEGER,
    character_name VARCHAR(150),
    character_image TEXT
);

-- Datos de prueba
INSERT INTO "user" (username, email, password)
VALUES ('admin', 'admin@example.com', 'hashed_password');

INSERT INTO task (title, description, due_date, status, user_id)
VALUES ('Tarea de ejemplo', 'Esta es una tarea de prueba', '2025-12-31', 'Pendiente', 1);
