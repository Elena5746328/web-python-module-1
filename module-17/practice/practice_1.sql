CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC(10, 2) CHECK (salary > 0),
    department_id INT REFERENCES departments(id),
    hired_at DATE DEFAULT CURRENT_DATE
);

CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    employee_id INT REFERENCES employees(id),
    budget NUMERIC(12, 2) CHECK (budget >= 0),
    is_active BOOLEAN DEFAULT TRUE
);

INSERT INTO departments (name)
VALUES
    ('IT'),
    ('HR'),
    ('Finance'),
    ('Marketing');

INSERT INTO employees (name, salary, department_id, hired_at)
VALUES
    ('Анна Иванова', 150000, 1, '2023-01-15'),
    ('Иван Петров', 90000, 1, '2023-03-10'),
    ('Мария Смирнова', 110000, 2, '2022-11-20'),
    ('Олег Кузнецов', 130000, 3, '2021-06-05'),
    ('Алексей Орлов', 70000, NULL, '2024-02-01'),
    ('Елена Соколова', 160000, 1, '2020-09-12');

INSERT INTO projects (name, employee_id, budget, is_active)
VALUES
    ('CRM System', 1, 500000, TRUE),
    ('Website Redesign', 2, 200000, TRUE),
    ('Hiring Platform', 3, 300000, TRUE),
    ('Accounting Automation', 4, 350000, FALSE),
    ('Internal Chat', 1, 150000, TRUE);

