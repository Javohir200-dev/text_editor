CREATE DATABASE editor;

use editor;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Уникальный ID пользователя
    username VARCHAR(100) UNIQUE NOT NULL,   -- Имя пользователя (уникальное)
    email VARCHAR(255) UNIQUE NOT NULL,      -- Email пользователя (уникальный)
    password VARCHAR(255) NOT NULL,          -- Хеш пароля
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Дата и время регистрации
);

CREATE TABLE documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY, -- Уникальный ID документа
    user_id INT,                                -- ID пользователя, который создал документ
    title VARCHAR(255) NOT NULL,                -- Заголовок документа
    content TEXT NOT NULL,                     -- Содержимое документа (все данные будут храниться как текст)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Время создания документа
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Время последнего обновления
    FOREIGN KEY (user_id) REFERENCES users(user_id) -- Внешний ключ, ссылающийся на таблицу пользователей
);

INSERT INTO users (username, email, password) 
VALUES ('john_doe', 'john@example.com', 'hashed_password_here');

