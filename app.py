from flask import Flask, jsonify, after_this_request
from flask_login import LoginManager
import os
from dotenv import load_dotenv
load_dotenv() # takes the environment variables from .env

from resources.wine import wine
from resources.user import user

import models

from flask_cors import CORS
DEBUG = True
PORT=os.environ.get("PORT")
login_manager = LoginManager()

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")
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


@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)


@app.route('/')
def index():
    return 'hello'

# ADD THESE THREE LINES -- because we need to initialize the
# tables in production too!
print(os.environ, 'os.environ')
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()
   

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)