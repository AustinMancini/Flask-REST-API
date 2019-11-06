from flask import Flask, Blueprint, jsonify, request, render_template, url_for, redirect
from server import db
from models import Post, PostForm

api_bp = Blueprint('api_bp', __name__)

# Routes
@api_bp.route('/addpost', methods=['GET', 'POST'])
def add_post():
    postform = PostForm()
    if request.method == 'POST':
        pf = Post(
            postform.title.data,
            postform.post_text.data,
        )
        db.session.add(pf)
        db.session.commit()
        return render_template('success.html')
    return render_template('post_form.html', postform=postform)
