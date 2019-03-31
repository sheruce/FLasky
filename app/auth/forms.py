from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('password', validators=[DataRequired()])
    rember_me = BooleanField('keep me logged in')
    submit = SubmitField('log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[DataRequired, Length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                          0, 'Username must have only '
                                                             'letters,numbers,dots or'
                                                             'undersocres')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_usernmae(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
