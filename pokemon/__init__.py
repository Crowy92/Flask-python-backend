from unicodedata import name
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from .routes.main import main_routes

#db stuff
from dotenv import load_dotenv
from .database.db import db
from os import environ
# Load environment variables
load_dotenv()
database_uri = environ.get('DATABASE_URL')
#set up the app
app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)
CORS(app)
# link the db and the app
db.app = app
db.init_app(app)

app.register_blueprint(main_routes)

@app.route('/')
def welcome():
    return 'Welcome to Flask!'

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    print(err)
    return jsonify({"message": f"It's not you it's us", "error": err}), 500

if __name__ == "__main__":
    app.run(debug=True)

