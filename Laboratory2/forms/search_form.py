from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators


class SearchForm(FlaskForm):
    type_field = SelectField('choose field', choices=[
        ('vacancy_name', 'vacancy_name'),
        ('vacancy_company', 'vacancy_company'),
        ('vacancy_location', 'vacancy_location'),
        ('vacancy_employment', 'vacancy_employment'),
        ('vacancy_salary', 'vacancy_salary')
    ])
    search_value = StringField("value: ", [validators.DataRequired('shouldnt be empty value')])

    submit = SubmitField("search")
