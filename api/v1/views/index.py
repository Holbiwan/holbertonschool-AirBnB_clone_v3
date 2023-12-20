#!/usr/bin/python3
"""Defines routing for the Flask application"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON response with the status of the API"""
    return jsonify({"status": "OK"})
