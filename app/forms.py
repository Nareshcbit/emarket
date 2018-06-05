from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
 
class ContactForm(FlaskForm):
  name = StringField("Name")
  email = StringField("Email")
  subject = StringField("Subject")
  message = StringField("Message")
  submit = SubmitField("Send")

class UserForm(FlaskForm):
  username = StringField("Name")
  email = StringField("Email")
  submit = SubmitField("Send")