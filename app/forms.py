from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
 
class AddItemsForm(FlaskForm):
  Vendor = StringField("Vendor")
  Category = StringField("Category")
  Model = StringField("Model")
  Price = IntegerField("Price")
  submit = SubmitField("Submit")

class SearchItemsForm(FlaskForm):
  Vendor = StringField("Vendor")
  Category = StringField("Category")
  Model = StringField("Model")
  submit = SubmitField("Search")

