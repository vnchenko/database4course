# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask
#
# app = Flask(__name__)
# app.secret_key = 'key'
#
# ENV = 'dev'
#
# if ENV == 'dev':
#     app.debug = True
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/postgres'
# else:
#     app.debug = False
#     app.config[
#         'SQLALCHEMY_DATABASE_URI'] = 'postgres://efbqxjbrcsobam:a690b8f821f8e746598f7dd92f7602e29ffc85c14485e16822895e277d3f99f9@ec2-174-129-10-235.compute-1.amazonaws.com:5432/d4md2h2t2e3mk5'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# db = SQLAlchemy(app)
#
#
# class OrmSkill(db.Model):
#     __tablename__ = 'orm_skill'
#
#     skill_name = db.Column(db.String(20), primary_key=True)
#     user_email = db.Column(db.String(20), db.ForeignKey('orm_user.user_email'))
#
#
# class UserHasVacancy(db.Model):
#     __tablename__ = 'user_has_vacancy'
#     user_email = db.Column(db.String(20), db.ForeignKey('orm_user.user_email'), primary_key=True)
#     vacancy_id = db.Column(db.Integer, db.ForeignKey('orm_vacancy.vacancy_id'), primary_key=True)
#
#
# class OrmCriterion(db.Model):
#     __tablename__ = 'orm_criterion'
#
#     criterion_name = db.Column(db.String(20), primary_key=True)
#
#     vacancy_id = db.Column(db.Integer, db.ForeignKey('orm_vacancy.vacancy_id'))
#
#
# class OrmVacancy(db.Model):
#     __tablename__ = 'orm_vacancy'
#
#     vacancy_id = db.Column(db.Integer, primary_key=True)
#     vacancy_company = db.Column(db.String(20), nullable=False)
#     vacancy_name = db.Column(db.String(30), nullable=False)
#     vacancy_location = db.Column(db.String(30), nullable=False)
#     vacancy_employment = db.Column(db.String(15), nullable=False)
#     vacancy_salary = db.Column(db.Integer, nullable=False)
#
#     user_email_fk = db.relationship('OrmUser', secondary='user_has_vacancy')
#     vacancy_criterions = db.relationship('OrmCriterion')
#
#
# # class UserHasCity(db.Model):
# #     __tablename__ = 'user_has_city'
# #     user_email = db.Column(db.String(20), db.ForeignKey('orm_user.user_email'), primary_key=True)
# #     city_name = db.Column(db.String(20), db.ForeignKey('orm_city.city_name'), primary_key=True)
#
#
# class OrmUser(db.Model):
#     __tablename__ = 'orm_user'
#
#     user_email = db.Column(db.String(20), primary_key=True)
#     user_name = db.Column(db.String(20), nullable=False)
#     user_phone = db.Column(db.String(15), nullable=False)
#     user_birthday = db.Column(db.Date, nullable=False)
#     user_location = db.Column(db.String(30), nullable=False)
#     user_employment = db.Column(db.String(15), nullable=False)
#
#     user_skills = db.relationship('OrmSkill')
#     vacancy_id_fk = db.relationship('OrmVacancy', secondary='user_has_vacancy')
#     # city_name_fk = db.relationship('OrmCity', secondary='user_has_city')
#
#
# # class OrmCity(db.Model):
# #     __tablename__ = 'orm_city'
# #
# #     city_name = db.Column(db.String(20), primary_key=True)
# #     city_population = db.Column(db.Integer, primary_key=False)
# #     city_coord = db.Column(db.String(20), nullable=False)
# #     city_year = db.Column(db.Date, nullable=False)
# #     user_email_fk = db.relationship('OrmUser', secondary='user_has_city')
