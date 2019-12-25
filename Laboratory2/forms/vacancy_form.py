from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators


class VacancyForm(FlaskForm):
    vacancy_name = StringField("Vacancy name: ", [
        validators.DataRequired("Please enter vacancy name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    vacancy_company = StringField("Company name: ", [
        validators.DataRequired("Please enter company name."),
    ])
    vacancy_location = StringField("Vacancy location: ", [
        validators.DataRequired("Please enter your phone."),
        validators.Length(3, 15)
    ])
    vacancy_employment = StringField("Vacancy employment: ", [
        validators.DataRequired("Please enter your location."),
        validators.Length(3, 30)
    ])
    vacancy_salary = IntegerField("Vacancy salary: ", [
        validators.DataRequired("Please enter your location.")
    ])

    submit = SubmitField("Save")

    def validate_salary(self):
        return bool(self.vacancy_salary.data > 499)
