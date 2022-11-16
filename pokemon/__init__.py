from unicodedata import name
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from .routes.main import main_routes

app = Flask(__name__)
CORS(app)

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

