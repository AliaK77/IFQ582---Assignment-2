from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.fields import SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, email

class LoginForm(FlaskForm):
    """Form for user login."""
    email = StringField("Email", validators = [InputRequired(), email()])
    password = PasswordField("Password", validators = [InputRequired()])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    """Form for user registration."""
    firstname = StringField("Your first name", validators = [InputRequired()])
    lastname = StringField("Your surname", validators = [InputRequired()])
    email = StringField("Email", validators = [InputRequired(), email()])
    phone = StringField("Your phone number", validators = [InputRequired()])
    password = PasswordField("Password", validators = [InputRequired()])
    submit = SubmitField("Make Account")

class UpdateItemForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image_link = FileField('Add an Image', validators=[FileAllowed(['jpg', 'png'])])
    item_category = StringField('Category', validators=[InputRequired()])
    cultural_group = StringField('Cultural Group', validators=[InputRequired()])
    sensitivity_notes = TextAreaField('Sensitivity Notes', validators=[InputRequired()])
    review_status = TextAreaField('Review Status', validators=[InputRequired()])
    access_level = StringField('Access Level', validators=[InputRequired()])
    submit = SubmitField('Post')  
    