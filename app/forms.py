from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, widgets
from wtforms.validators import DataRequired


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class SimpleForm(FlaskForm):
    fruits = ['apple', 'banana', 'cherry']  # Ejemplo de lista
    alco = ['rum', 'vodka', 'whiskey']  # Ejemplo de lista
    nonalco = ['juice', 'soda', 'water']  # Ejemplo de lista
    others = ['ice', 'mint', 'lemon']  # Ejemplo de lista

    fruits = sorted(fruits)
    alco = sorted(alco)
    nonalco = sorted(nonalco)
    others = sorted(others)

    # Crear una lista de tuplas de valor/descripción
    fruit_list = [(x.title(), x.title()) for x in fruits if x != '']
    alco_list = [(x.title(), x.title()) for x in alco if x != '']
    nonalco_list = [(x.title(), x.title()) for x in nonalco if x != '']
    others_list = [(x.title(), x.title()) for x in others if x != '']

    fruits_cb = SelectMultipleField('Fruits', choices=fruit_list)
    alco_cb = SelectMultipleField('Alcoholic', choices=alco_list)
    nonalco_cb = SelectMultipleField('Non-Alcoholic', choices=nonalco_list)
    others_cb = SelectMultipleField('Others', choices=others_list)

    search = StringField('Search')
    submit = SubmitField('Submit')


class NavbarForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Submit')

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    search = StringField('Search')  
    submit = SubmitField('Submit')
    

class YourForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    search = StringField('Search')
    submit = SubmitField('Submit')