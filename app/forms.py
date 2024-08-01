from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, RadioField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    ingredients = StringField('Ingredients', validators=[DataRequired()])
    steps = StringField('Steps', validators=[DataRequired()])
    time = StringField('Time', validators=[DataRequired()])
    submit = SubmitField('Добавить')