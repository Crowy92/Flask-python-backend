from unicodedata import name
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

lemurs = [
    {
        "id": 1,
        "name": "larry"
    },
    {
        "id": 2,
        "name": "jemima"
    }
]
@app.route('/')
def welcome():
    return 'Welcome to Flask!'

@app.route('/lemur', methods=['GET', 'POST'])
def lemurs_handler():
    if request.method == 'GET':
        return jsonify(lemurs), 200
    elif request.method == 'POST':
        new_lemur = request.json
        last_id = lemurs[-1]['id']
        new_lemur['id'] = last_id + 1
        lemurs.append(new_lemur)
        return f"You created a lemur! IT's name is {new_lemur['name']}", 201

@app.route('/lemur/<int:lemur_id>', methods=['GET'])
def lemur_handler(lemur_id):
    try: 
        return next(lemur for lemur in lemurs if lemur['id'] == lemur_id)
    except:
        raise exceptions.BadRequest(f"We do not have a lemur with that id: {lemur_id}")

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"It's not you it's us"}), 500

if __name__ == "__main__":
    app.run(debug=True)

