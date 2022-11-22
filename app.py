from unicodedata import name
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

pokemons = [
    { 
        "id": 1, 
        "name": 'Bulbasaur', 
        "frontImg": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png", 
        "moves": ["vine whip", "razor leaf", "tackle"] 
    },
    { 
        "id": 2, 
        "name": 'Charmander', 
        "frontImg": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png", 
        "moves": ["ember", "scratch", "leer"] 
    },
    { 
        "id": 3, 
        "name": 'Squirtle', 
        "frontImg": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png", 
        "moves": ["bubble", "water gun", "withdraw"]  
    },
];

@app.route('/')
def welcome():
    return 'Welcome to Flask!'

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemons_handler():
    if request.method == 'GET':
        return jsonify(pokemons), 200
    elif request.method == 'POST':
        new_pokemon = request.json
        last_id = pokemons[-1]['id']
        new_pokemon['id'] = last_id + 1
        pokemons.append(new_pokemon)
        return new_pokemon, 201

@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def pokemon_handler(pokemon_id):
    try: 
        return next(pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id)
    except:
        raise exceptions.BadRequest(f"We do not have a pokemon with that id: {pokemon_id}")

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"message": f"Oops... {err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"message": f"It's not you it's us"}), 500

if __name__ == "__main__":
    app.run(debug=True)

