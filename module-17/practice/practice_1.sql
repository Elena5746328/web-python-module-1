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

-------------

SELECT 
    name,
    salary,
    CASE 
        WHEN salary >= 150000 THEN 'high'
        WHEN salary >= 100000 THEN 'middle'
        ELSE 'low'
    END AS salary_level
FROM employees;

-------------

SELECT
    e.name AS employee_name, 
    coalesce(d.name, 'Без отдела') AS department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-------------

SELECT
    d.id, 
    d.name
FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e
    WHERE e.department_id = d.id
);

-------------

SELECT
    d.id,
    d.name
FROM employees e
WHERE EXISTS (
    SELECT 1 FROM projects p
    WHERE p.employee_id = e.id
)

-------------

SELECT
    name AS projects_name,
    budget,
    CASE
        WHEN is_active = true THEN 'active'
        else 'close'
    END AS project_status
FROM projects;

-------------

SELECT
    e.name AS employee_name,
    COUNT(p.id) AS projects_count
FROM employees e
LEFT JOIN projects p ON p.employee_id = e.id
GROUP BY e.id, e.name
ORDER BY projects_count DESC;

-------------

UPDATE projects
SET budget = budget + 50000
WHERE is_active = TRUE;
RETURNING id, name, budget, is_active;

-------------

DELETE FROM projects
WHERE is_active = FALSE
RETURNING id, name;