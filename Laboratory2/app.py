from flask import Flask, render_template, request, redirect
from forms.user_form import UserForm
from forms.vacancy_form import VacancyForm
from forms.user_edit_form import UserFormEdit
from forms.skill_form import Skill
from forms.skill_edit_form import SkillEdit
from forms.criterion_edit import CriterionEdit
import uuid
import json
import plotly
from sqlalchemy.sql import func
import plotly.graph_objs as go
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'key'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/postgres'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://efbqxjbrcsobam:a690b8f821f8e746598f7dd92f7602e29ffc85c14485e16822895e277d3f99f9@ec2-174-129-10-235.compute-1.amazonaws.com:5432/d4md2h2t2e3mk5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class OrmSkill(db.Model):
    __tablename__ = 'orm_skill'

    skill_name = db.Column(db.String(20), primary_key=True)
    user_email = db.Column(db.String(20), db.ForeignKey('orm_user.user_email'))


class UserHasVacancy(db.Model):
    __tablename__ = 'user_has_vacancy'
    user_email = db.Column(db.String(20), db.ForeignKey('orm_user.user_email'), primary_key=True)
    vacancy_id = db.Column(db.Integer, db.ForeignKey('orm_vacancy.vacancy_id'), primary_key=True)


class OrmCriterion(db.Model):
    __tablename__ = 'orm_criterion'

    criterion_name = db.Column(db.String(20), primary_key=True)

    vacancy_id = db.Column(db.Integer, db.ForeignKey('orm_vacancy.vacancy_id'))


class OrmVacancy(db.Model):
    __tablename__ = 'orm_vacancy'

    vacancy_id = db.Column(db.Integer, primary_key=True)
    vacancy_company = db.Column(db.String(20), nullable=False)
    vacancy_name = db.Column(db.String(30), nullable=False)
    vacancy_location = db.Column(db.String(30), nullable=False)
    vacancy_employment = db.Column(db.String(15), nullable=False)
    vacancy_salary = db.Column(db.Integer, nullable=False)

    user_email_fk = db.relationship('OrmUser', secondary='user_has_vacancy')
    vacancy_criterions = db.relationship('OrmCriterion')


class OrmUser(db.Model):
    __tablename__ = 'orm_user'

    user_email = db.Column(db.String(20), primary_key=True)
    user_name = db.Column(db.String(20), nullable=False)
    user_phone = db.Column(db.String(15), nullable=False)
    user_birthday = db.Column(db.Date, nullable=False)
    user_location = db.Column(db.String(30), nullable=False)
    user_employment = db.Column(db.String(15), nullable=False)

    user_skills = db.relationship('OrmSkill')
    vacancy_id_fk = db.relationship('OrmVacancy', secondary='user_has_vacancy')

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
#     vacancy_id=123,
#     vacancy_company='convidera',
#     vacancy_name='convidera frontend',
#     vacancy_location='Kyiv',
#     vacancy_employment='full-time',
#     vacancy_salary=1000
# )
# vacancy_2 = OrmVacancy(
#     vacancy_id=234,
#     vacancy_company='google',
#     vacancy_name='google backend',
#     vacancy_location='Kyiv',
#     vacancy_employment='full-time',
#     vacancy_salary=1000
# )
# vacancy_3 = OrmVacancy(
#     vacancy_id=345,
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
#     firefighter_skill,
#     frontend_criterion,
#     backend_criterion,
#     designer_criterion
# ])
# # # commit
# db.session.commit()


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/users')
def users():
    res = db.session.query(OrmUser).all()

    return render_template('users_table.html', users=res)


@app.route('/skills')
def skills():
    res = db.session.query(OrmSkill).all()

    return render_template('skills_table.html', skills=res)


@app.route('/vacancies')
def vacancies():
    res = db.session.query(OrmVacancy).all()

    return render_template('vacancies_table.html', vacancies=res)


@app.route('/criterions')
def criterions():
    res = db.session.query(OrmCriterion).all()

    return render_template('criterions_table.html', criterions=res)


@app.route('/create_user', methods=['POST', 'GET'])
def create_user():
    form = UserForm()

    if request.method == 'POST':
        new_user = OrmUser(
            user_name=form.user_name.data,
            user_birthday=form.user_birthday.data.strftime("%Y-%m-%d"),
            user_email=form.user_email.data,
            user_phone=form.user_phone.data,
            user_location=form.user_location.data,
            user_employment=form.user_employment.data
        )
        db.session.add(new_user)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('user_form.html', form=form)


@app.route('/create_vacancy', methods=['POST', 'GET'])
def create_vacancy():
    form = VacancyForm()

    if request.method == 'POST':
        new_vacancy = OrmVacancy(
            vacancy_company=form.vacancy_company.data,
            vacancy_name=form.vacancy_name.data,
            vacancy_location=form.vacancy_location.data,
            vacancy_employment=form.vacancy_employment.data,
            vacancy_salary=form.vacancy_salary.data,
            vacancy_id=uuid.uuid1().clock_seq_hi_variant
        )
        db.session.add(new_vacancy)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('vacancy_form.html', form=form)


@app.route('/edit_skill/<string:email>/<string:skill>', methods=['GET', 'POST'])
def edit_skill(email, skill):
    form = SkillEdit()
    result = db.session.query(OrmSkill).filter(OrmSkill.user_email == email).filter(OrmSkill.skill_name == skill).one()

    if request.method == 'GET':

        form.skill_name.data = result.skill_name

        return render_template('skill.html', form=form, form_name='edit skill')
    elif request.method == 'POST':

        result.skill_name = form.skill_name.data

        db.session.commit()
        return redirect('/skills')


@app.route('/user_edit/<string:email>', methods=['GET', 'POST'])
def edit_user(email):
    form = UserFormEdit()
    result = db.session.query(OrmUser).filter(OrmUser.user_email == email).one()

    if request.method == 'GET':

        form.user_name.data = result.user_name
        form.user_birthday.data = result.user_birthday
        form.user_phone.data = result.user_phone
        form.user_location.data = result.user_location
        form.user_employment.data = result.user_employment
        form.user_email.data = result.user_email

        return render_template('edit_user.html', form=form, form_name='edit user')
    elif request.method == 'POST':

        result.user_name = form.user_name.data
        result.user_birthday = form.user_birthday.data.strftime("%Y-%m-%d"),
        result.user_phone = form.user_phone.data
        result.user_location = form.user_location.data
        result.user_employment = form.user_employment.data

        db.session.commit()
        return redirect('/users')


@app.route('/vacancy_edit/<string:vac_id>', methods=['GET', 'POST'])
def vacancy_edit(vac_id):
    form = VacancyForm()
    result = db.session.query(OrmVacancy).filter(OrmVacancy.vacancy_id == int(vac_id)).one()

    if request.method == 'GET':

        form.vacancy_name.data = result.vacancy_name
        form.vacancy_company.data = result.vacancy_company
        form.vacancy_location.data = result.vacancy_location
        form.vacancy_employment.data = result.vacancy_employment
        form.vacancy_salary.data = result.vacancy_salary

        return render_template('vacancy_form.html', form=form, form_name='edit vacancy')
    elif request.method == 'POST':

        result.vacancy_name = form.vacancy_name.data
        result.vacancy_company = form.vacancy_company.data,
        result.vacancy_location = form.vacancy_location.data
        result.vacancy_employment = form.vacancy_employment.data
        result.vacancy_salary = form.vacancy_salary.data

        db.session.commit()
        return redirect('/vacancies')


@app.route('/criterion_edit/<string:vac_id>/<string:name>', methods=['GET', 'POST'])
def criterion_edit(vac_id, name):
    form = CriterionEdit()
    result = db.session.query(OrmCriterion).filter(OrmCriterion.vacancy_id == vac_id).filter(
        OrmCriterion.criterion_name == name).one()

    if request.method == 'GET':

        form.criterion_name.data = result.criterion_name

        return render_template('criterion_edit.html', form=form, form_name=vac_id)
    elif request.method == 'POST':

        result.criterion_name = form.criterion_name.data

        db.session.commit()
        return redirect('/criterions')


@app.route('/new_skill/<string:email>', methods=['GET', 'POST'])
def new_skill(email):
    form = Skill()

    if request.method == 'POST':
        new_skill = OrmSkill(
            skill_name=form.skill_name.data,
            user_email=email
        )
        db.session.add(new_skill)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        form.user_email.data = email
        return render_template('skill.html', form=form)


@app.route('/new_criterion/<string:vac_id>', methods=['GET', 'POST'])
def new_criterion(vac_id):
    form = CriterionEdit()

    if request.method == 'POST':
        new_criterion = OrmCriterion(
            criterion_name=form.criterion_name.data,
            vacancy_id=int(vac_id)
        )
        db.session.add(new_criterion)
        db.session.commit()
        return render_template('success.html')
    elif request.method == 'GET':
        return render_template('criterion_edit.html', form=form)


@app.route('/delete_user/<string:email>', methods=['GET', 'POST'])
def delete_user(email):
    result = db.session.query(OrmUser).filter(OrmUser.user_email == email).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


@app.route('/delete_vacancy/<string:vac_id>', methods=['GET', 'POST'])
def delete_vacancy(vac_id):
    result = db.session.query(OrmVacancy).filter(OrmVacancy.vacancy_id == int(vac_id)).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


@app.route('/delete_criterion/<string:vac_id>/<string:name>', methods=['GET', 'POST'])
def delete_criterion(vac_id, name):
    result = db.session.query(OrmCriterion).filter(OrmCriterion.vacancy_id == vac_id).filter(
        OrmCriterion.criterion_name == name).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


@app.route('/delete_skill/<string:email>/<string:skill>', methods=['GET', 'POST'])
def delete_skill(email, skill):
    result = db.session.query(OrmSkill).filter(OrmSkill.user_email == email).filter(OrmSkill.skill_name == skill).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    query1 = (
        db.session.query(
            OrmUser.user_name,
            func.count(OrmSkill.skill_name).label('skill_name')
        ).join(OrmSkill, OrmUser.user_email == OrmSkill.user_email).
            group_by(OrmUser.user_name)
    ).all()

    query2 = (
        db.session.query(
            OrmVacancy.vacancy_name,
            func.count(OrmCriterion.criterion_name).label('criterion_name')
        ).join(OrmCriterion, OrmCriterion.vacancy_id == OrmVacancy.vacancy_id).
            group_by(OrmVacancy.vacancy_name)
    ).all()

    user_name, skill_count = zip(*query1)
    bar = go.Bar(
        x=user_name,
        y=skill_count
    )

    vacancy_name, criterion_count = zip(*query2)
    pie = go.Pie(
        labels=vacancy_name,
        values=criterion_count
    )

    data = {
        "bar": [bar],
        "pie": [pie]
    }
    graphs_json = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard.html', graphsJSON=graphs_json)


if __name__ == "__main__":
    app.run()
