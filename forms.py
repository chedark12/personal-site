from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForms
class AddProjectForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    description = StringField("Project Description", validators=[DataRequired()])
    url = StringField("Project URL", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Project")
