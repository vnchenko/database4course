from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators


class SkillEdit(FlaskForm):
    skill_name = StringField("skill name: ", [
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    submit = SubmitField("Save")
