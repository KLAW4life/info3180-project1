from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired

class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    bedroom = StringField('No. of Rooms', validators=[InputRequired()])
    bathroom = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price', validators=[InputRequired()])
    type = SelectField('Property Type', validators=[InputRequired()], choices=[("House","House"), ("Apartment", "Apartment")])
    location = StringField('Location', validators=[InputRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Image Files Only!')])

