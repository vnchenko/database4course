CREATE KEYSPACE IF NOT EXISTS labwork1 WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': '1'
};

CREATE TYPE IF NOT EXISTS labwork1.user_name_type (
 first_name text,
 last_name text
);

CREATE TABLE IF NOT EXISTS labwork1."User_Vacancy_Skill_Criterion" (
 user_email text,
 user_name frozen<labwork1.user_name_type>,
 user_phone LIST<frozen<SET<text>>>,
 user_birthday text,
 user_location list<text>,
 user_employment text,
 user_location_count int STATIC,
 
 skill_name text,
 
 vacancy_company text,
 vacancy_name text,
 vacancy_location text,
 vacancy_employment text,
 vacancy_salary int,
 
 criterion_name text,
 PRIMARY KEY ((user_email), skill_name, vacancy_company, criterion_name)
);
