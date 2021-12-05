from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Email

class SignupForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class FlashCardForm(FlaskForm):
    front = StringField('Front', validators=[DataRequired()])
    back = StringField('Back', validators=[DataRequired()])
    submit = SubmitField('Create')

class EventsForm(FlaskForm):
    event = StringField('Event', validators=[DataRequired()])
    day = DateField('Day', format = '%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Create Event')

class ProjectsForm(FlaskForm):
    completed_proj = IntegerField('Completed', validators = [DataRequired()])
    uncompleted_proj = IntegerField('Uncompleted', validators = [DataRequired()])
    submit = SubmitField('Add Hours')
