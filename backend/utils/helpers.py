# backend/utils/helpers.py

import re
from flask import jsonify

def validate_email(email):
    """Validate the email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def api_response(success=True, message="", data=None, status_code=200):
    """Generate a standardized JSON response for the API."""
    response = {
        "success": success,
        "message": message,
        "data": data
    }
    return jsonify(response), status_code

def hash_password(password):
    """Hash a password for storing."""
    # Placeholder for password hashing function, e.g., bcrypt or werkzeug.security
    pass

def check_password(password_hash, password):
    """Verify a stored password against one provided by user"""
    # Placeholder for password check function
    pass
