-- db/init_users.sql
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE users ADD COLUMN full_name VARCHAR(100);

-- Insérer un utilisateur admin par défaut (mot de passe à changer)
INSERT INTO users (username, password, email)
VALUES ('admin', 'motdepasse', 'admin@gmail.com')
ON DUPLICATE KEY UPDATE password='motdepasse'