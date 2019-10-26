from flask import render_template, request, redirect
from forms.user_form import UserForm
from forms.vacancy_form import VacancyForm
from forms.user_edit_form import UserFormEdit
from forms.skill_form import Skill
from forms.skill_edit_form import SkillEdit
from forms.criterion_edit import CriterionEdit
from dao.orm.populate import *
from flask import Flask
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/postgres'
db = SQLAlchemy(app)
app.secret_key = 'development key'


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


if __name__ == "__main__":
    app.run()
