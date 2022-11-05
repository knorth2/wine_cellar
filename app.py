from flask import Flask, jsonify
from flask_login import LoginManager

from resources.wine import wine
from resources.user import user

import models

from flask_cors import CORS
DEBUG = True
PORT=8000
login_manager = LoginManager()

app = Flask(__name__)

app.secret_key = "ASDFASDFASDFASDF"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except:
        return None


CORS(wine, origins=['http://localhost:3000'], supports_credentials=True)
CORS(user, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(wine, url_prefix='/api/v1/wine')
app.register_blueprint(user, url_prefix='/api/v1/user')

@app.route('/')
def index():
    return 'hello'

    

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)