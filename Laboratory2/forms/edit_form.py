from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class UserFormEdit(FlaskForm):
    user_name = StringField("Name: ", [validators.Length(3, 20, "Name should be from 3 to 20 symbols")])
    user_birthday = DateField("Birthday: ")
    user_email = HiddenField("Email: ", [validators.Email("Wrong email format")])
    user_phone = StringField("Phone: ", [validators.Length(15)])
    user_location = StringField("Your location: ", [validators.Length(30)])
    user_employment = StringField("Your employment: ", [validators.Length(15)])

    submit = SubmitField("Save")
