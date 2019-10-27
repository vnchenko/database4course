# from dao.orm.model import *
#
# db.create_all()
#
# db.session.query(UserHasVacancy).delete()
# db.session.query(OrmCriterion).delete()
# db.session.query(OrmSkill).delete()
# db.session.query(OrmVacancy).delete()
# db.session.query(OrmUser).delete()
#
# # создане объектов
# Bob = OrmUser(
#     user_email='bob@gmail.com',
#     user_name="Bob",
#     user_phone="380665583447",
#     user_birthday='10-10-2000',
#     user_location="Kyiv",
#     user_employment="full-time"
# )
#
# Boba = OrmUser(
#     user_email='boba@gmail.com',
#     user_name="Boba",
#     user_phone="380665583448",
#     user_birthday='10-10-2000',
#     user_location='Borispol',
#     user_employment='part-time'
# )
# Boban = OrmUser(
#     user_email='boban@gmail.com',
#     user_name="Boban",
#     user_phone="380665583449",
#     user_birthday='10-10-2000',
#     user_location='Moskow',
#     user_employment='full-time'
# )
#
# frontend_skill = OrmSkill(
#     skill_name='frontend'
# )
#
# firefighter_skill = OrmSkill(
#     skill_name='firefighter_skill'
# )
#
# backend_skill = OrmSkill(
#     skill_name='backend'
# )
#
# designer_skill = OrmSkill(
#     skill_name='design'
# )
#
# # create relations User - Skills
#
# Bob.user_skills.append(frontend_skill)
# Bob.user_skills.append(firefighter_skill)
# # Bob.user_skills.append(designer)
#
# Boba.user_skills.append(backend_skill)
# # Boba.user_skills.append(backend)
# # Boba.user_skills.append(designer)
#
# Boban.user_skills.append(designer_skill)
# # Boban.user_skills.append(backend)
# # Boban.user_skills.append(designer)
#
# vacancy_1 = OrmVacancy(
#     vacancy_id=1,
#     vacancy_company='convidera',
#     vacancy_name='convidera frontend',
#     vacancy_location='Kyiv',
#     vacancy_employment='full-time',
#     vacancy_salary=1000
# )
# vacancy_2 = OrmVacancy(
#     vacancy_id=2,
#     vacancy_company='google',
#     vacancy_name='google backend',
#     vacancy_location='Kyiv',
#     vacancy_employment='full-time',
#     vacancy_salary=1000
# )
# vacancy_3 = OrmVacancy(
#     vacancy_id=3,
#     vacancy_company='facebook',
#     vacancy_name='facebook designer',
#     vacancy_location='Kyiv',
#     vacancy_employment='full-time',
#     vacancy_salary=1000
# )
#
# Bob.vacancy_id_fk.append(vacancy_1)
#
# Boba.vacancy_id_fk.append(vacancy_2)
#
# Boban.vacancy_id_fk.append(vacancy_3)
#
# frontend_criterion = OrmCriterion(
#     criterion_name='frontend'
# )
#
# backend_criterion = OrmCriterion(
#     criterion_name='backend'
# )
#
# designer_criterion = OrmCriterion(
#     criterion_name='design'
# )
#
# vacancy_1.vacancy_criterions.append(frontend_criterion)
# vacancy_2.vacancy_criterions.append(backend_criterion)
# vacancy_3.vacancy_criterions.append(designer_criterion)
#
# # insert into database
# db.session.add_all([
#     Bob,
#     Boba,
#     Boban,
#     vacancy_1,
#     vacancy_2,
#     vacancy_3,
#     frontend_skill,
#     backend_skill,
#     designer_skill,
#     frontend_criterion,
#     backend_criterion,
#     designer_criterion
# ])
# # # commit
# db.session.commit()
