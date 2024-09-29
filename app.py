from flask import Flask,jsonify,request
from flask_cors import CORS
import requests

app=Flask(__name__)
CORS(app)

@app.route('/api/get_anime/', methods=['POST'])
def get_anime():
    anime_name= request.json.get('name')
    if not anime_name:
        return jsonify({"error": "Anime name is required"})
    response = requests.get(f'https://api.jikan.moe/v4/anime?q={anime_name}')
    data=response.json()
    return jsonify(ok=True, response=data), 200

@app.route('/api/get_anime/<int:mal_id>/', methods=['GET'])
def get_anime_details(mal_id):
    response = requests.get(f'https://api.jikan.moe/v4/anime/{mal_id}')
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch anime details"}), response.status_code
    
    data = response.json()
    return jsonify(ok=True, response=data), 200

if __name__ == '__main__':
    app.run(debug=True)


