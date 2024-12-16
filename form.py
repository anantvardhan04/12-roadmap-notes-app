# Used flask_wtf extension to create a form
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class NoteForm(FlaskForm):
    file = FileField("Upload File", validators=[DataRequired()])
    submit = SubmitField("Submit")
