INSERT INTO labwork1."User_Vacancy_Skill_Criterion" (
 user_email,
 user_name,
 user_phone,
 user_birthday,
 user_location,
 user_employment,
 user_location_count,
 skill_name,
 vacancy_company,
 vacancy_name,
 vacancy_location,
 vacancy_employment,
 vacancy_salary,
 criterion_name
 ) VALUES (
  'ioann.vnchenko@gmail.com',
  {"first_name": 'Ivan', "last_name": 'Vovchenko'},
  [{'380665583447', '380966460616'}],
  '24.02.1999',
  ['Kyiv'],
  'full-time',
  1,
  'frontend',
  'Convidera',
  'frontend convidera',
  'Koln',
  'full-time',
  1000,
  'frontend'
 );
 
INSERT INTO labwork1."User_Vacancy_Skill_Criterion" (
 user_email,
 user_name,
 user_phone,
 user_birthday,
 user_location,
 user_employment,
 user_location_count,
 skill_name,
 vacancy_company,
 vacancy_name,
 vacancy_location,
 vacancy_employment,
 vacancy_salary,
 criterion_name
 ) VALUES (
  'yarok1999@gmail.com',
  {"first_name": 'Yaroslav', "last_name": 'Artemenko'},
  [{'0977730222'}],
  '11.08.1999',
  ['Zigen', 'Kyiv'],
  'full-time',
  2,
  'doc-writer',
  'Convidera',
  'co convidera',
  'Zigen',
  'part-time',
  700,
  'doc-writer'
 );
 
INSERT INTO labwork1."User_Vacancy_Skill_Criterion" (
 user_email,
 user_name,
 user_phone,
 user_birthday,
 user_location,
 user_employment,
 user_location_count,
 skill_name,
 vacancy_company,
 vacancy_name,
 vacancy_location,
 vacancy_employment,
 vacancy_salary,
 criterion_name
 ) VALUES (
  'vladkaneve@gmail.com',
  {"first_name": 'Vlad', "last_name": 'Kanevskiy'},
  [{'0502436247'}],
  '12.12.1998',
  ['Kyiv', 'Berbuchiv'],
  'full-time',
  2,
  'backend',
  'Epam',
  'backend epam',
  'Kyiv',
  'full-time',
  500,
  'beckend'
 );

SELECT * FROM labwork1."User_Vacancy_Skill_Criterion";


UPDATE labwork1."User_Vacancy_Skill_Criterion"
SET user_name = { first_name: 'Ivan', last_name: 'Vovk' }
WHERE
 user_email = 'ioann.vnchenko@gmail.com' AND
 skill_name = 'frontend' AND
 vacancy_company = 'Convidera' AND
 criterion_name = 'frontend';
 
UPDATE labwork1."User_Vacancy_Skill_Criterion"
SET user_employment = 'part-time'
WHERE
 user_email = 'yarok1999@gmail.com' AND
 skill_name = 'doc-writer' AND
 vacancy_company = 'Convidera' AND
 criterion_name = 'doc-writer';
 
UPDATE labwork1."User_Vacancy_Skill_Criterion"
SET vacancy_salary = 2000
WHERE
 user_email = 'vladkaneve@gmail.com' AND
 skill_name = 'backend' AND
 vacancy_company = 'Epam' AND
 criterion_name = 'beckend';
 
SELECT * FROM labwork1."User_Vacancy_Skill_Criterion";

SELECT user_name
FROM labwork1."User_Vacancy_Skill_Criterion"
WHERE skill_name = 'frontend';

SELECT user_location
FROM labwork1."User_Vacancy_Skill_Criterion"
WHERE user_name = {"first_name": 'Vlad', "last_name": 'Kanevskiy'};

SELECT user_email
FROM labwork1."User_Vacancy_Skill_Criterion"
WHERE vacancy_salary = 2000;


DELETE user_location
FROM labwork1."User_Vacancy_Skill_Criterion"
WHERE
 user_email = 'ioann.vnchenko@gmail.com' AND
 skill_name = 'frontend' AND
 vacancy_company = 'Convidera' AND
 criterion_name = 'frontend';
 
DELETE vacancy_name
FROM labwork1."User_Vacancy_Skill_Criterion"
WHERE
 user_email = 'yarok1999@gmail.com' AND
 skill_name = 'doc-writer' AND
 vacancy_company = 'Convidera' AND
 criterion_name = 'doc-writer';

DELETE user_birthday
FROM labwork1."User_Vacancy_Skill_Criterion"
WHERE
 user_email = 'vladkaneve@gmail.com' AND
 skill_name = 'backend' AND
 vacancy_company = 'Epam' AND
 criterion_name = 'beckend';
 
SELECT * FROM labwork1."User_Vacancy_Skill_Criterion";
