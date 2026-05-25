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

-------------
create table employee_profiles (
	id SERIAL primary key,
	employee_id INT unique references employees(id),
	phone TEXT unique,
	address TEXT,
	birth_date DATE
);

insert into employee_profiles(employee_id, phone, address, birth_date)
values
	(1, '+70000000003', 'address-1', '1980-05-25'),
	(2, '+70000000002', 'address-1', '1981-05-25'),
	(3, '+70000000001', 'address-1', '1982-05-25');

select 
	e.name as employee_name,
	ep.phone,
	ep.address,
	ep.birth_date
from employees e
join employee_profiles ep on ep.employee_id = e.id;

insert into employee_profiles(employee_id, phone, address, birth_date)
values 
	(1, '+70000000003', 'address-4', '1995-05-25');

----------------------------
-- N - N
create table skills (
	id SERIAL primary key,
	name TEXT not null unique 
);

create table employee_skills (
	employee_id INT references employees(id),
	skill_id int references skills(id),
	primary key (employee_id, skill_id)
);

insert into skills (name)
values 
	('SQL'),
	('PostgreSQL'),
	('MySQL'),
	('Excel');

insert into employee_skills (employee_id, skill_id)
values 
	(1, 1),
	(2, 1),
	(3, 1),
	(1, 2),
	(2, 2),
	(3, 2),
	(1, 4);
	
select
	e.name as employee_name, 
	s.name as skill_name
from employee_skills es
join employees e on es.employee_id = e.id
join skills s on es.skill_id = s.id
order by e.name, s.name;

----------------------------

select 
	e.name as employee_name,
	e.salary,
	d.name as department_name,
	ep.phone,
	ep.address,
	p.name as project_name,
	s.name as skill_name
from employees e
left join employee_profiles ep on e.id = ep.employee_id
left join departments d on d.id = e.department_id
left join projects p on p.employee_id = e.id
left join employee_skills es on es.employee_id = e.id
left join skills s on es.skill_id = s.id;

----------------------------

select 
	e.name as employee_name,
	coalesce(SUM(p.budget),0) as total_budget
from employees e
left join projects p on e.id = p.employee_id
group by e.id, e.name
order by e.name

----------------------------

select
	p.name as project_name,
	p.budget,
	e.name as employee_name,
	d.name as department_name
from employees e
join projects p on p.employee_id = e.id
join departments d on d.id = e.department_id
where
	e.status = 'active' and p.budget > 200000 