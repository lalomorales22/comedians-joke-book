from flask import Flask, jsonify
from flask_cors import CORS
from database.db_config import close_db_connection  # Adjusted to absolute import
from api.joke_routes import joke_routes  # Adjusted to absolute import

app = Flask(__name__)
CORS(app)

app.register_blueprint(joke_routes, url_prefix='/api')

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500

@app.teardown_appcontext
def shutdown_session(exception=None):
    close_db_connection()

if __name__ == '__main__':
    app.run(debug=True)
