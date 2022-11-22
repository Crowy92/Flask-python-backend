from flask import Blueprint, request, jsonify
from ..database.pokemon import pokemons
from werkzeug import exceptions
from ..models.pokemon import Pokemon
from ..database import db

main_routes = Blueprint("main", __name__)

@main_routes.route('/pokemon', methods=['GET', 'POST'])
def pokemons_handler():
    if request.method == 'GET':
        pokemons = Pokemon.query.all()
        print(pokemons)
        return jsonify(pokemons), 200
    elif request.method == 'POST':
        pData = request.json
        new_pokemon = Pokemon(name=pData["name"], frontImg=pData["frontImg"], move1=pData["move1"])
        db.session.add(new_pokemon)
        db.session.commit()
        return jsonify(pData), 201

@main_routes.route('/pokemon/<int:pokemon_id>', methods=['GET', 'DELETE'])
def pokemon_handler(pokemon_id):
    if request.method == 'GET':
        try: 
            return next(pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id)
        except:
            raise exceptions.BadRequest(f"We do not have a pokemon with that id: {pokemon_id}")
    elif request.method == 'DELETE':
        try:
            del pokemons[pokemon_id -1]
            return jsonify(pokemons), 204
        except:
            raise exceptions.BadRequest(f"failed to delete pokemon with htat id: {pokemon_id}")
