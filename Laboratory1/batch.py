from cassandra.cluster import Cluster

cluster = Cluster()
connection = cluster.connect('labwork1')

batch = """
BEGIN BATCH
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
 
APPLY BATCH;
"""
connection.execute(batch)