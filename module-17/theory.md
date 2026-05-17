# Модуль 17.Введение в работу с базами данных

## 1. DDL — создание и изменение структуры

### `CREATE`
Создаёт объект: таблицу, базу, индекс, представление и т.д.
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    salary NUMERIC
);
```

---

### `TABLE`
Указывает, что создаётся или изменяется таблица.
```sql 
CREATE TABLE departments (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

---

### `ALTER`
Изменяет существующий объект.
```sql
ALTER TABLE employees
ADD COLUMN email TEXT;
```

---

### `ADD`
Добавляет колонку, ограничение и т.д.
```sql
ALTER TABLE employees
ADD COLUMN phone TEXT;
```

---

### `DROP`
Удаляет объект.
```sql
DROP TABLE projects;
```

---

### `IF EXISTS`
Позволяет избежать ошибки, если объекта нет.
```sql
DROP TABLE IF EXISTS old_projects;
```

---

### `IF NOT EXISTS`
Создаёт объект только если он ещё не существует.
```sql
CREATE TABLE IF NOT EXISTS departments (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

---

### `RENAME`
Переименовывает объект.
```sql
ALTER TABLE employees
RENAME COLUMN name TO full_name;
```

---

### `TRUNCATE`
Быстро очищает таблицу.
```sql
TRUNCATE TABLE projects;
```

---

### `CASCADE`
Удаляет зависимые объекты.
```sql
DROP TABLE departments CASCADE;
```

---

### `RESTRICT`
Запрещает удаление, если есть зависимости.
```sql
DROP TABLE departments RESTRICT;
```


## 2. DML — работа с данными

### `INSERT`
Добавляет строки.
```sql
INSERT INTO departments (name)
VALUES ('IT'), ('HR'), ('Finance');
```

---

### `INTO`
Указывает, куда вставлять данные.
```sql
INSERT INTO employees (name, salary, department_id)
VALUES ('Анна', 120000, 1);
```

---

### `VALUES`

Передаёт конкретные значения.
```sql
INSERT INTO projects (name, employee_id, budget)
VALUES ('CRM System', 1, 500000);
```

---

### `SELECT`
Выбирает данные.
```sql
SELECT name, salary
FROM employees;
```

---

### `FROM`
Указывает источник данных.
```sql
SELECT *
FROM employees;
```