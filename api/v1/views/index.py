#!/usr/bin/python3
"""
Index route for API version 1.
This module defines the index route for the API version 1.
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def status():
    """
    Status route.

    This route returns the status of the API.
    Returns:
        A JSON response with the status of the API.
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    Stats route.

    This route returns the count of each object type.
    Returns:
        A JSON response with the count of each object type.
    """
    counts = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(counts)
