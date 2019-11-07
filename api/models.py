from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from run import db

class Post(db.Model):
    # __tablename__ = 'post'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(80), unique=True)
    post_text = db.Column(db.String(255))

    def __init__(self, title, post_text):
        self.title = title
        self.post_text = post_text


# Declaring Flask WTF-Form
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    post_text = StringField('Post_Text', validators=[DataRequired()])
