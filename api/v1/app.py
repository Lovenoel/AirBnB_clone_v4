#!/usr/bin/python3
"""
Flask application instance for API version 1.
This module creates and configures the Flask application instance,
registers the necessary blueprints, and sets up the teardown context.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# Create an instance of the Flask class
app = Flask(__name__)

# Register the blueprint for API views
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Close the current storage session.

    This method is called when the app context tears down. It ensures
    that the storage session is closed properly.
    """
    storage.close()

if __name__ == "__main__":
    # Run the Flask application
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
