from flask import Blueprint, request, render_template, jsonify
from ..database.pokemon import pokemons
from werkzeug import exceptions
# from ..models.listing import Listing

main_routes = Blueprint("main", __name__)

@main_routes.route('/pokemon', methods=['GET', 'POST'])
def pokemons_handler():
    if request.method == 'GET':
        return jsonify(pokemons), 200
    elif request.method == 'POST':
        new_pokemon = request.json
        last_id = pokemons[-1]['id']
        new_pokemon['id'] = last_id + 1
        pokemons.append(new_pokemon)
        return new_pokemon, 201

@main_routes.route('/pokemon/<int:pokemon_id>', methods=['GET', 'DELETE'])
def pokemon_handler(pokemon_id):
    if request.method == 'GET':
        try: 
            return next(pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id)
        except:
            raise exceptions.BadRequest(f"We do not have a pokemon with that id: {pokemon_id}")
    elif request.method == 'DELETE':    
        try:
            del pokemons[pokemon_id - 1]
            return jsonify(pokemons), 204
        except:
            raise exceptions.BadRequest(f"failed to delete pokemon with that id: {pokemon_id}")