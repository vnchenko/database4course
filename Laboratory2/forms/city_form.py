from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators


class CityForm(FlaskForm):
    city_name = StringField("City name: ", [
        validators.DataRequired("Please enter city name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    city_population = IntegerField("city population: ", [
        validators.NumberRange(min=1)
    ])
    city_coord = StringField("city coord: ", [validators.DataRequired("Please enter coord.")])
    city_year = DateField("city birthday: ", [validators.DataRequired("Please enter city birthday.")])

    submit = SubmitField("Save")
