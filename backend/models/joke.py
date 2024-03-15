# backend/models/joke.py

from bson import ObjectId
from datetime import datetime
from pymongo import ReturnDocument
from backend.database.db_config import joke_collection

class Joke:
    def __init__(self, joke_name, joke_description, percentage=0, love_it=0, created_at=None):
        self.joke_name = joke_name
        self.joke_description = joke_description
        self.percentage = percentage
        self.love_it = love_it
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            'joke_name': self.joke_name,
            'joke_description': self.joke_description,
            'percentage': self.percentage,
            'love_it': self.love_it,
            'created_at': self.created_at
        }

    @staticmethod
    def create_joke(joke_data):
        joke = Joke(**joke_data)
        result = joke_collection.insert_one(joke.to_dict())
        return str(result.inserted_id)

    @staticmethod
    def get_joke(joke_id):
        joke_data = joke_collection.find_one({'_id': ObjectId(joke_id)})
        if joke_data:
            return Joke(**joke_data)
        return None

    @staticmethod
    def update_joke(joke_id, update_data):
        update_data['updated_at'] = datetime.utcnow()
        updated_joke = joke_collection.find_one_and_update(
            {'_id': ObjectId(joke_id)},
            {'$set': update_data},
            return_document=ReturnDocument.AFTER
        )
        if updated_joke:
            return Joke(**updated_joke)
        return None

    @staticmethod
    def delete_joke(joke_id):
        result = joke_collection.delete_one({'_id': ObjectId(joke_id)})
        return result.deleted_count > 0