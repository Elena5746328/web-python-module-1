-- Задание 1
CREATE DATABASE Birds;
USE Birds;

-- Задание 2
CREATE DATABASE Cats;
DROP DATABASE Birds;
USE Cats;

-- Задание 3
DROP DATABASE Cats;

-- Задание 4
CREATE DATABASE VegetablesAndFruits;
USE VegetablesAndFruits;

CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(10)
);

INSERT INTO categories (id, name) VALUES
    (1, 'овощ'),
    (2, 'фрукт');

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    category_id INT,
    color VARCHAR(20),
    calories INT,
    description TEXT
);

INSERT INTO products (id, name, category_id, color, calories, description) VALUES
    (1, 'Яблоко', 2, 'красный', 52, 'Сладкий фрукт, богат железом и витаминами.'),
    (2, 'Морковь', 1, 'оранжевый', 41, 'Сочный корнеплод, полезен для зрения.'),
    (3, 'Банан', 2, 'жёлтый', 89, 'Тропический фрукт, источник калия.'),
    (4, 'Огурец', 1, 'зелёный', 15, 'Низкокалорийный овощ, часто используется в салатах.'),
    (5, 'Апельсин', 2, 'оранжевый', 47, 'Цитрус, богат витамином C.'),
    (6, 'Помидор', 1, 'красный', 18, 'Часто ошибочно считается фруктом, на самом деле овощ.'),
    (7, 'Киви', 2, 'зелёный', 61, 'Экзотический фрукт с пушистой кожурой.'),
    (8, 'Капуста белокочанная', 1, 'зелёный', 25, 'Источник клетчатки и витамина C.'),
    (9, 'Лимон', 2, 'жёлтый', 29, 'Кислый цитрус, используется для напитков и кулинарии.');

-- Задание 5
SELECT * FROM products;

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'овощ';

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'фрукт';

SELECT name FROM products;

SELECT DISTINCT color FROM products;

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'фрукт' AND p.color = 'жёлтый';

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'овощ' AND p.color = 'красный';

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'овощ' AND p.calories < 50;

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'фрукт' AND p.calories BETWEEN 60 AND 100;

SELECT * FROM products
WHERE description LIKE '%витамин%';

SELECT * FROM products
WHERE color IN ('жёлтый', 'красный');

SELECT COUNT(*) AS vegetable_count
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'овощ';

SELECT COUNT(*) AS fruit_count
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'фрукт';

SELECT ROUND(AVG(calories), 2) AS avg_calories FROM products;

SELECT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.name = 'фрукт'
ORDER BY p.calories ASC
LIMIT 1;