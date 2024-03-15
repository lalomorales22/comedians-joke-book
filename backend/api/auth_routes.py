# backend/api/auth_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from backend.models.user import User

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    if User.find_by_username(username):
        return jsonify({"msg": "Username already exists"}), 409

    user = User.create_user(username, email, password)
    return jsonify({"msg": "User created", "user": {"username": user.username, "email": user.email}}), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    user = User.find_by_username(username)
    if user and user.verify_password(password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad username or password"}), 401

@auth_routes.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    # JWT logout is handled client-side by removing the token from storage.
    return jsonify({"msg": "Logged out"}), 200

# Add this blueprint in your app.py or where you initialize your Flask app
# app.register_blueprint(auth_routes, url_prefix='/api/auth')
