#!/usr/bin/python3
"""
Blueprint for API version 1 views.
This module initializes the blueprint for the API version 1 views and imports the routes.
"""

from flask import Blueprint

# Create a Blueprint instance for API views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import the index module to register routes
from api.v1.views.index import *
