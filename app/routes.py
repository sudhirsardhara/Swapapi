from flask import jsonify, request
from app import app, cache, db
from models import CachedResponse
import requests

@cache.memoize()
def fetch_data(endpoint):
    response = requests.get(f"{app.config['SWAPI_BASE_URL']}/{endpoint}")
    return response.json()

@app.route('/api/<resource>', methods=['GET'])
def get_swapi_resource(resource):
    try:
        data = fetch_data(resource)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/<resource>/search', methods=['GET'])
def search_swapi_resource(resource):
    query = request.args.get('q')
    try:
        data = fetch_data(resource)
        if query:
            data = [item for item in data['results'] if query.lower() in item['name'].lower()]
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/<resource>/sort', methods=['GET'])
def sort_swapi_resource(resource):
    try:
        data = fetch_data(resource)
        data['results'] = sorted(data['results'], key=lambda x: x.get('name', ''))
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500