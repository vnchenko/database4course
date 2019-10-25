from flask import render_template, request, redirect
from forms.user_form import UserForm
from forms.edit_form import UserFormEdit
from dao.orm.populate import *


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/users')
def users():
    res = db.session.query(OrmUser).all()

    return render_template('users_table.html', users=res)


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


@app.route('/delete_user/<string:email>', methods=['GET', 'POST'])
def delete_user(email):
    result = db.session.query(OrmUser).filter(OrmUser.user_email == email).one()

    db.session.delete(result)
    db.session.commit()

    return render_template('success.html')


if __name__ == "__main__":
    app.run()
