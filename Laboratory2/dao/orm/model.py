from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/postgres'
db = SQLAlchemy(app)
app.secret_key = 'development key'


class OrmUser(db.Model):
    __tablename__ = 'orm_user'

    user_email = db.Column(db.String(20), primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_phone = db.Column(db.String(15), nullable=False)
    user_birthday = db.Column(db.Date, nullable=False)
    user_location = db.Column(db.String(30), nullable=False)
    user_employment = db.Column(db.String(15), nullable=False)

    user_skills = db.relationship('OrmSkill')
    user_vacancies = db.relationship('OrmVacancy')


class OrmSkill(db.Model):
    __tablename__ = 'orm_skill'

    skill_name = db.Column(db.String(20), primary_key=True)
    user_email = db.Column(db.String(20), ForeignKey('orm_user.user_email'))


class OrmVacancy(db.Model):
    __tablename__ = 'orm_vacancy'

    vacancy_id = db.Column(db.Integer, primary_key=True)
    vacancy_company = db.Column(db.String(20), nullable=False)
    vacancy_name = db.Column(db.String(30), nullable=False)
    vacancy_location = db.Column(db.String(30), nullable=False)
    vacancy_employment = db.Column(db.String(15), nullable=False)
    vacancy_salary = db.Column(db.Integer, nullable=False)

    user_email = db.Column(db.String(20), ForeignKey('orm_user.user_email'))
    vacancy_criterions = db.relationship('OrmCriterion')


class OrmCriterion(db.Model):
    __tablename__ = 'orm_criterion'

    criterion_name = db.Column(db.String(20), primary_key=True)

    vacancy_id = db.Column(db.Integer, ForeignKey('orm_vacancy.vacancy_id'))
    # company = db.relationship('OrmSkill', back_populates='orm_criterion')

    # OrmVacancy.criterions = db.relationship('OrmCriterion', back_populates='orm_vacancy')
