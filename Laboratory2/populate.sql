insert into "User" (user_email, user_name, user_phone, user_birthday, user_location, user_employment) values ('Ivan@gmail.com', 'Ivan', '380665588441', '12-12-99', 'Kyiv', 'full-time');

insert into "User" (user_email, user_name, user_phone, user_birthday, user_location, user_employment) values ('yaroslav@gmail.com', 'Yaroslav', '380775588441', '11-11-99', 'Zmerinka', 'full-time');

insert into "User" (user_email, user_name, user_phone, user_birthday, user_location, user_employment) values ('dog@gmail.com', 'Vladik', '380995588441', '10-01-98', 'Boyarka', 'part-time');

insert into "User" (user_email, user_name, user_phone, user_birthday, user_location, user_employment) values ('vadim@gmail.com', 'vadim', '380225588441', '09-10-99', 'Borispol', 'part-time');

insert into "User" (user_email, user_name, user_phone, user_birthday, user_location, user_employment) values ('vitalya@gmail.com', 'vitalya', '380115588441', '08-09-01', 'Selo', 'part-time');

insert into Skill (skill_name, user_email) values ('front-end', 'vadim@gmail.com');

insert into Skill (skill_name, user_email) values ('devops', 'dog@gmail.com');

insert into Skill (skill_name, user_email) values ('backend', 'vadim@gmail.com');

insert into Skill (skill_name, user_email) values ('firefighter', 'dog@gmail.com');

insert into Skill (skill_name, user_email) values ('ui/ux', 'vadim@gmail.com');

insert into Vacancy (vacancy_company, vacancy_name, user_email, vacancy_location, vacancy_employment, vacancy_salary) values ('jcash', 'devops jcash', 'yaroslav@gmail.com', 'Kyiv', 'full-time', 1000);

insert into Vacancy (vacancy_company, vacancy_name, user_email, vacancy_location, vacancy_employment, vacancy_salary) values ('convidera', 'frontend convidera', 'Ivan@gmail.com', 'Kyiv', 'full-time', 1200);

insert into Vacancy (vacancy_company, vacancy_name, user_email, vacancy_location, vacancy_employment, vacancy_salary) values ('google', 'backend google', 'dog@gmail.com', 'Kyiv', 'part-time', 1000);

insert into Vacancy (vacancy_company, vacancy_name, user_email, vacancy_location, vacancy_employment, vacancy_salary) values ('facebook', 'devops facebook', 'Ivan@gmail.com', 'Kyiv', 'part-time', 900);

insert into Vacancy (vacancy_company, vacancy_name, user_email, vacancy_location, vacancy_employment, vacancy_salary) values ('kpi', 'student', 'yaroslav@gmail.com', 'Kyiv', 'part-time', 2000);

insert into Criterion (criterion_name, vacancy_company, vacancy_name) values ('python', 'six', 'backend');

insert into Criterion (criterion_name, vacancy_company, vacancy_name) values ('node', 'epam', 'backend');

insert into Criterion (criterion_name, vacancy_company, vacancy_name) values ('html', 'jcash', 'koi student');

insert into Criterion (criterion_name, vacancy_company, vacancy_name) values ('js', 'convidera', 'frontend convidera');

insert into Criterion (criterion_name, vacancy_company, vacancy_name) values ('css', '6ix9ine', 'backend');

