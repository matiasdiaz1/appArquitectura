# views/UserView.py
from flask import Blueprint, jsonify
from models.UserModel import User

user_blueprint = Blueprint('user', __name__)

# Ruta para obtener todos los usuarios
@user_blueprint.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()  # Traemos todos los usuarios de la base de datos
    return jsonify([user.username for user in users])

# Ruta para obtener un usuario por ID
@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username})
    else:
        return jsonify({'message': 'User not found'}), 404
