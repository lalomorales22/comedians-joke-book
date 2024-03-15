# backend/database/db_config.py

from pymongo import MongoClient

# MongoDB connection string
MONGO_URI = 'mongodb+srv://laloadrianmorales:zx7IdxKe4EnvWwJW@clusterphug.cpyhmmd.mongodb.net/?retryWrites=true&w=majority'

# Create a MongoDB client
client = MongoClient(MONGO_URI)

# Get the database instance
db = client['comedian_joke_app']

# Get the jokes collection
joke_collection = db['jokes']

# Function to close the database connection
def close_db_connection():
    client.close()
