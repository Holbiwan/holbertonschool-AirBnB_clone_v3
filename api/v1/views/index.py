#!/usr/bin/python3
"""Defines routing for the Flask application"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON response with the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON response with the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each object type"""
    stats_dict = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User"),
    }
    return jsonify(stats_dict)
