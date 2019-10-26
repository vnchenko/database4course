from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators


class Skill(FlaskForm):
    skill_name = StringField("skill name: ", [validators.Length(3, 20, "Name should be from 3 to 20 symbols")])
    user_email = StringField("Email: ", [validators.DataRequired("Please enter your name."),
                                         validators.Email("Wrong email format")])

    submit = SubmitField("Save")
