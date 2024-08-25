from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional



class DonorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=100)])
    blood_group = SelectField('Blood Group', choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], validators=[DataRequired()])
    units_available = IntegerField('Units Available', validators=[DataRequired(), NumberRange(min=1)])
    has_transmissible_disease = BooleanField('Has Transmissible Disease')
    health_conditions = TextAreaField('Health Conditions (Comma Separated)', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Submit')

class RecipientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    blood_group = SelectField('Blood Group', choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], validators=[DataRequired()])
    units_needed = IntegerField('Units Needed', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Submit')