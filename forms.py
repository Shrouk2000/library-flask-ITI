from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    cover_photo = FileField('Cover Photo', validators=[DataRequired()])
    number_of_pages = IntegerField('Number of Pages', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
