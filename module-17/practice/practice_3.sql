drop database  if exists Academy;
create database Academy;

create table Faculties (
    Id SERIAL primary key,
    Financing DECIMAL(10,2) not null default 0 check (Financing >= 0),
    Name VARCHAR(100) not null unique,
    Dean VARCHAR(255) not null
);

create table Departments (
    Id SERIAL primary key,
    Financing DECIMAL(10,2) not null default 0 check (Financing >= 0),
    Name VARCHAR(100) not null unique,
    FacultyId INT not null,
    foreign key (FacultyId) references Faculties(Id)
);

create table Groups (
    Id SERIAL primary key,
    Name VARCHAR(10) not null unique ,
    Year INT not null check (Year between 1 and 5),
    Rating INT not null check (Rating between 0 and 5), 
    DepartmentId INT not null,
    foreign key (DepartmentId) references Departments(Id)
);

create table Teachers (
    Id SERIAL primary key ,
    Name VARCHAR(255) not null ,
    Surname VARCHAR(255) not null ,
    Salary DECIMAL(10,2) not null check (Salary > 0),
    EmploymentDate DATE not null check (EmploymentDate >= '1990-01-01'),
    Position VARCHAR(255) not null ,
    IsAssistant BOOLEAN,
    IsProfessor BOOLEAN,
    Premium DECIMAL(10,2) not null default 0 check (Premium >= 0)
);

create table Curators (
    Id SERIAL primary key,
    Name VARCHAR(255),
    Surname VARCHAR(255)
);

create table Subjects (
    Id SERIAL primary key ,
    Name VARCHAR(100) not null unique
);

create table Lectures (
    Id SERIAL primary key ,
    LectureRoom VARCHAR(255) not null ,
    SubjectId INT not null ,
    TeacherId INT not null ,
    foreign  key (SubjectId) references Subjects(Id),
    foreign  key (TeacherId) references Teachers(Id)
);

create table GroupsCurators (
    Id SERIAL primary key,
    CuratorId INT not null,
    GroupId INT not null,
    foreign key (CuratorId) references Curators(Id),
    foreign key (GroupId) references Groups(Id),
    constraint uc_group_curator unique (GroupId, CuratorId)
);

create table GroupsLectures (
    Id SERIAL primary key,
    GroupId INT not null ,
    LectureId INT not null ,
    foreign key (GroupId) references Groups(Id),
    foreign key (LectureId) references Lectures(Id)
);

insert into Faculties (Name, Financing, Dean) values
('Computer Science', 500000, 'John Smith'),
('Mathematics', 450000, 'Anna Johnson'),
('Physics', 400000, 'Peter Brown');

insert into Departments (Name, Financing, FacultyId) values
('Programming', 200000, 1),
('Database Theory', 180000, 1),
('Applied Math', 150000, 2);

insert into groups (Name, Year, DepartmentId, Rating) values
('P107', 3, 1, 4),
('M201', 2, 3, 3),
('P305', 4, 2, 5),
('G501', 5, 1, 3),
('G502', 5, 2, 2);

insert into Teachers (Name, Surname, Salary, EmploymentDate, Position, IsAssistant, IsProfessor, Premium) 
values
('Samantha', 'Adams', 1200, '2015-09-01', 'Professor', false, true, 200),
('Michael', 'Johnson', 1100, '2016-07-15', 'Associate Professor', false, false, 150),
('Anna', 'Smith', 1300, '2014-03-22', 'Professor', false, true, 250),
('David', 'Wilson', 110, '2020-01-15', 'Assistant', true, false, 20),
('Emma', 'Taylor', 90, '2021-03-10', 'Assistant', true, false, 15),
('Robert', 'Clark', 800, '1995-06-20', 'Professor', false, true, 100);

insert into Curators (Name, Surname) values
('John', 'Doe'),
('Alice', 'Brown');

insert into Subjects (Name) values
('Database Theory'),
('Programming Fundamentals'),
('Algorithms');

insert into Lectures (LectureRoom, SubjectId, TeacherId) values
('B103', 1, 1),
('A201', 2, 2),
('C305', 3, 3);

insert into GroupsCurators (CuratorId, GroupId) values
(1, 1),
(2, 2);

insert into GroupsLectures (GroupId, LectureId) values
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(5, 2);

insert into Lectures (LectureRoom, SubjectId, TeacherId) values
('B103', 1, 3),
('A201', 2, 1),
('C305', 3, 2);

insert into GroupsLectures (GroupId, LectureId) values
(1, 4),
(2, 5),
(3, 6),
(4, 4),
(5, 5);

-- Задача 1
select
    Name,
    Financing,
    Id
from Departments;

-- Задача 2
select
    Groups.Name as GroupName,
    Groups.Rating as GroupRating
from Groups;

-- Задача 3
select
    Surname,
    ROUND((Premium / Salary) * 100, 2) as PremiumPercent,
    ROUND((Salary / (Salary + Premium)) * 100, 2) as SalaryPercent
from Teachers;

-- Задача 4
select
    CONCAT('The dean of faculty ', Name, ' is ', Dean) as FacultyDean
from Faculties;

-- Задача 5
select Surname 
from Teachers 
where IsProfessor = true 
and Salary > 1050;

-- Задача 6
select Name 
from Departments 
where Financing < 11000 
or Financing > 25000;

-- Задача 7
select
    Name
from Faculties
where Name <> 'Computer Science';

-- Задача 8
select
    Surname,
    Position
from Teachers
where IsProfessor = false;

-- Задача 9
select Surname, Position, Salary, Premium 
from Teachers 
where IsAssistant = true 
and Premium >= 160 
and Premium <= 550;

-- Задача 10
select Surname, Salary 
from Teachers 
where IsAssistant = true;

-- Задача 11
select Surname, Position 
from Teachers 
where EmploymentDate < '2000-01-01';

-- Задача 12
select Name as NameOfDepartment 
from Departments 
where Name < 'Software Development';

-- Задача 13
select Surname 
from Teachers 
where IsAssistant = true 
and (Salary + Premium) <= 1200;

-- Задача 14
select Name 
from Groups 
where Year = 5 
and Rating >= 2 
and Rating <= 4;

-- Задача 15
select Surname 
from Teachers 
where IsAssistant = true
and (Salary < 550 or Premium < 200);

------------------------------------------

-- Задача 1
select
    CONCAT(T.Name, ' ', T.Surname) as Teacher,
    G.Name as GroupName
from Teachers T
cross join Groups G
order by Teacher;

-- Задача 2
select
    F.Name as FacultyName
from Faculties F
where exists (
    select 1
    from Departments D
    where D.FacultyId = F.Id
      and D.Financing > F.Financing
);

-- Задача 3
select
    C.Surname as CuratorSurname,
    G.Name as GroupName
from Curators C
join GroupsCurators GC on C.Id = GC.CuratorId
join Groups G on GC.GroupId = G.Id
order by CuratorSurname;

-- Задача 4
select
    CONCAT(T.Name, ' ', T.Surname) as TeacherName
from Teachers T
join Lectures L on T.Id = L.TeacherId
join GroupsLectures GL on L.Id = GL.LectureId
join Groups G on GL.GroupId = G.Id
where G.Name = 'P107';

-- Задача 5
select
    T.Surname as TeacherSurname,
    F.Name as FacultyName
from Teachers T
join Lectures L on T.Id = L.TeacherId
join Subjects S on L.SubjectId = S.Id
join GroupsLectures GL on L.Id = GL.LectureId
join Groups G on GL.GroupId = G.Id
join Departments D on G.DepartmentId = D.Id
join Faculties F on D.FacultyId = F.Id
group by T.Id, T.Surname, F.Name;

-- Задача 6
select
    D.Name as DepartmentName,
    G.Name as GroupName
from Departments D
join Groups G on D.Id = G.DepartmentId
order by DepartmentName;

-- Задача 7
select
    S.Name as SubjectName
from Subjects S
join Lectures L on S.Id = L.SubjectId
join Teachers T on L.TeacherId = T.Id
where T.Name = 'Samantha' and T.Surname = 'Adams';

-- Задача 8
select
    D.Name as DepartmentName
from Departments D
join Groups G on D.Id = G.DepartmentId
join GroupsLectures GL on G.Id = GL.GroupId
join Lectures L on GL.LectureId = L.Id
join Subjects S on L.SubjectId = S.Id
where S.Name = 'Database Theory';

-- Задача 9
select
    G.Name as GroupName
from Groups G
join Departments D on G.DepartmentId = D.Id
join Faculties F on D.FacultyId = F.Id
where F.Name = 'Computer Science';

-- Задача 10
select
    G.Name as GroupName,
    F.Name as FacultyName
from Groups G
join Departments D on G.DepartmentId = D.Id
join Faculties F on D.FacultyId = F.Id
where G.Year = 5;

-- Задача 11
select
    CONCAT(T.Name, ' ', T.Surname) as TeacherName,
    S.Name as SubjectName,
    G.Name as GroupName
from Teachers T
join Lectures L on T.Id = L.TeacherId
join Subjects S on L.SubjectId = S.Id
join GroupsLectures GL on L.Id = GL.LectureId
join Groups G on GL.GroupId = G.Id
where L.LectureRoom = 'B103';