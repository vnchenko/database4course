from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms import validators


class UserForm(FlaskForm):
    user_name = StringField("Name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    user_email = StringField("Email: ", [
        validators.DataRequired("Please enter your name."),
        validators.Email("Wrong email format")
    ])
    user_birthday = DateField("Birthday: ", [validators.DataRequired("Please enter your birthday.")])
    user_phone = StringField("Phone: ", [validators.DataRequired("Please enter your phone."),
                                         validators.Length(15)])
    user_location = StringField("Your location: ", [validators.DataRequired("Please enter your location."),
                                                    validators.Length(30)])
    user_employment = StringField("Your employment: ", [validators.DataRequired("Please enter your location."),
                                                        validators.Length(15)])

    submit = SubmitField("Save")
