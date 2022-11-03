from flask import Flask, jsonify
from flask_cors import CORS

from resources.wine import wine

import models

DEBUG = True
PORT= 8000


app = Flask(__name__)

CORS(wine, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(wine, url_prefix='/api/v1/wine')

@app.route('/')
def index():
    return 'hello'

    

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)