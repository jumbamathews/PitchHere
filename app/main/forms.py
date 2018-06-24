from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	description = TextAreaField("whats your pitch ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('promotion pitch','promotion pitch'), ('interview pitch','interview pitch'),('pickup lines','pickup lines'),('product pitch','product pitch'),])
	submit = SubmitField('Submit')

class CommentForm(FlaskForm):
	description = TextAreaField('',validators=[Required()])
	submit = SubmitField()