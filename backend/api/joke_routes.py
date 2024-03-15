# backend/api/joke_routes.py

from flask import Blueprint, request, jsonify
from backend.models.joke import Joke
from backend.services.audio_service import save_audio_file, delete_audio_file
from backend.services.transcription_service import transcribe_audio
from backend.services.language_model_service import extract_joke_info

joke_routes = Blueprint('joke_routes', __name__)

@joke_routes.route('/jokes', methods=['POST'])
def create_joke():
    audio_file = request.files.get('audio')
    if not audio_file:
        return jsonify({'error': 'No audio file provided'}), 400

    file_path = save_audio_file(audio_file, '/Users/smallbrain/Downloads/comedian_joke_app/uploads')
    if not file_path:
        return jsonify({'error': 'Invalid audio file'}), 400

    transcribed_text = transcribe_audio(file_path)
    joke_name, joke_description = extract_joke_info(transcribed_text)

    joke_data = {
        'joke_name': joke_name,
        'joke_description': joke_description,
        'audio_file_path': file_path
    }

    joke_id = Joke.create_joke(joke_data)
    delete_audio_file(file_path)

    return jsonify({'joke_id': joke_id}), 201

@joke_routes.route('/jokes/<joke_id>', methods=['GET'])
def get_joke(joke_id):
    joke = Joke.get_joke(joke_id)
    if not joke:
        return jsonify({'error': 'Joke not found'}), 404

    return jsonify(joke.to_dict()), 200

@joke_routes.route('/jokes/<joke_id>', methods=['PUT'])
def update_joke(joke_id):
    update_data = request.json
    updated_joke = Joke.update_joke(joke_id, update_data)
    if not updated_joke:
        return jsonify({'error': 'Joke not found'}), 404

    return jsonify(updated_joke.to_dict()), 200

@joke_routes.route('/jokes/<joke_id>', methods=['DELETE'])
def delete_joke(joke_id):
    success = Joke.delete_joke(joke_id)
    if not success:
        return jsonify({'error': 'Joke not found'}), 404

    return '', 204