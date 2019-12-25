from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators


class CompanyForm(FlaskForm):
    company_id = StringField("Company Id: ", [
        validators.DataRequired("Please enter company id."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    company_name = StringField("Company name: ", [
        validators.DataRequired("Please enter your name."),
        validators.Email("Wrong email format")
    ])
    company_address = StringField("Vacancy location: ", [validators.DataRequired("Please enter your phone."),
                                               validators.Length(15)])
    company_city = StringField("Vacancy employment: ", [validators.DataRequired("Please enter your location."),
                                                         validators.Length(30)])
    company_balance = IntegerField("Vacancy selary: ", [validators.DataRequired("Please enter your location."),
                                                       validators.Length(15)])

    submit = SubmitField("Save")
