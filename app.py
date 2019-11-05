from flask import Blueprint, jsonify, request
from server import db
from resources.models import User

api_bp = Blueprint('api_bp', __name__)

# Routes
@api_bp.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()

    new_user = User(name=user_data['name'], email=user_data['email'])

    db.session.add(new_user)
    db.session.commit()

    return 'Done', 201
