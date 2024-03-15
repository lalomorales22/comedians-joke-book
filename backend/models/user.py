# backend/models/user.py

from bson import ObjectId
from pymongo import HASHED
from werkzeug.security import generate_password_hash, check_password_hash
from backend.database.db_config import db

# Ensure indexing for username for faster query performance
db.users.create_index([('username', HASHED)])

class User:
    def __init__(self, username, email, password_hash=None, _id=None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self._id = _id or ObjectId()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            '_id': self._id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
        }

    @classmethod
    def create_user(cls, username, email, password):
        user = cls(username, email)
        user.password = password
        db.users.insert_one(user.to_dict())
        return user

    @classmethod
    def find_by_username(cls, username):
        data = db.users.find_one({'username': username})
        if data:
            return cls(**data)
        return None

    @classmethod
    def find_by_id(cls, _id):
        data = db.users.find_one({'_id': ObjectId(_id)})
        if data:
            return cls(**data)
        return None

    @classmethod
    def update_user(cls, _id, update_data):
        db.users.update_one({'_id': ObjectId(_id)}, {'$set': update_data})
        return cls.find_by_id(_id)

    @classmethod
    def delete_user(cls, _id):
        db.users.delete_one({'_id': ObjectId(_id)})
        return True
