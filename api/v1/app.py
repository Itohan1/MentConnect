#!/usr/bin/python3
""""""

import logging

logging.basicConfig(level=logging.DEBUG)
from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, render_template, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='static')
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
@app.teardown_appcontext
def close_db(error):
    """"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """"""
    return make_response(jsonify({'error': "Not found"}), 404)

if __name__ == "__main__":
    """"""
    host = environ.get("mentconnect_api_host")
    port = environ.get("mentconnect_api_port")
    if not host:
        host = "0.0.0.0"
    if not port:
        port = "5000"
    app.run(host=host, port=port, threaded=True, debug=True)
