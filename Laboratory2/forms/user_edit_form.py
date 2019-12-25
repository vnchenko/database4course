from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, HiddenField
from wtforms import validators


class UserFormEdit(FlaskForm):
    user_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    user_birthday = DateField("Birthday: ", [validators.DataRequired("Please enter your birthday.")])
    user_email = HiddenField("Email: ", [
        validators.Email("Wrong email format")
    ])
    user_phone = StringField("Phone: ", [
        validators.DataRequired("Please enter your phone."),
        validators.Length(10, 10)
    ])
    user_location = StringField("Your location: ", [
        validators.DataRequired("Please enter your location."),
        validators.Length(2, 30, "Name should be from 2 to 30 symbols")
    ])
    user_employment = StringField("Your employment: ", [
        validators.DataRequired("Please enter your location."),
        validators.Length(3, 15, "Name should be from 3 to 15 symbols")
    ])

    submit = SubmitField("Save")

    def validate_date(self):
        return bool(self.user_birthday.data.year > 1900)
