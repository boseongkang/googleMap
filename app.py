import json
from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

GOOGLE_BROWSER_KEY = os.getenv("GOOGLE_BROWSER_KEY")
GOOGLE_SERVER_KEY = os.getenv("GOOGLE_SERVER_KEY")


@app.route('/')
def home():
    return render_template('home.html', browser_key=GOOGLE_BROWSER_KEY)

@app.route('/results', methods=['GET', 'POST'])
def results():
    location = request.values.get('location')
    keyword = request.values.get('keyword')

    geo_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    geo_params = {'address': location, 'key': GOOGLE_SERVER_KEY}
    geo_resp = requests.get(geo_url, params=geo_params).json()
    if geo_resp.get('status') != 'OK' or not geo_resp.get('results'):
        return render_template('results.html', error='Invalid location', places=[],
                               center_json=json.dumps({'lat': 0, 'lng': 0}), location_text=location, keyword=keyword,
                               browser_key=GOOGLE_BROWSER_KEY)
    loc = geo_resp['results'][0]['geometry']['location']
    center_json = json.dumps(loc)

    places_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    place_params = {
        'key': GOOGLE_SERVER_KEY,
        'location': f"{loc['lat']},{loc['lng']}",
        'radius': 5000,
        'keyword': keyword,
        'language': 'en'
    }
    places_resp = requests.get(places_url, params=place_params).json()
    places = places_resp.get('results', [])

    return render_template('results.html',
                           center_json=center_json,
                           location_text=location,
                           keyword=keyword,
                           places=places,
                           browser_key=GOOGLE_BROWSER_KEY
                           )


@app.route('/map_search', methods=['POST'])
def map_search():
    data = request.json
    lat = data.get('lat')
    lng = data.get('lng')
    keyword = data.get('keyword')
    places_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    place_params = {
        'key': GOOGLE_SERVER_KEY,
        'location': f"{lat},{lng}",
        'radius': 5000,
        'keyword': keyword,
        'language': 'en'
    }
    places_resp = requests.get(places_url, params=place_params).json()
    places = places_resp.get('results', [])
    return jsonify({"places": places})


if __name__ == '__main__':
    app.run(debug=True)
