from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, DateField, SubmitField, BooleanField, PasswordField, FloatField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Email
from app.models import User, WeekData

class LoginForm(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember')
    submit = SubmitField('Submit')

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    birth = DateField('birth', validators=[DataRequired()])
    height = FloatField('height', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('submit')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('El email ya ha sido registrado. Por favor inicie sesion o ingrese otro email')


class WeekDataForm(FlaskForm):
    weight = FloatField('weight', validators=[DataRequired()])
    neck = FloatField('neck', validators=[DataRequired()])
    waist = FloatField('waist', validators=[DataRequired()])
    submit = SubmitField('submit')


