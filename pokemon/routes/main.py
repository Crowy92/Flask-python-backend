from flask import Blueprint, request, jsonify
# from ..database.pokemon import pokemons
from werkzeug import exceptions
from ..models.pokemon import Pokemon
from ..database.db import db

main_routes = Blueprint("main", __name__)

@main_routes.route('/pokemon', methods=['GET', 'POST'])
def pokemons_handler():
    if request.method == 'GET':
        pokemons = Pokemon.query.all()
        print('***************************')
        print(pokemons)
        outputs = map(lambda p: {"name": p.name, "frontImg": p.frontImg, "move1":p.move1}, pokemons)
        print(outputs)
        usableOutputs = list(outputs)
        return jsonify(usableOutputs), 200
    elif request.method == 'POST':
        pData = request.json
        new_pokemon = Pokemon(name=pData["name"], frontImg=pData["frontImg"], move1=pData["move1"])
        db.session.add(new_pokemon)
        db.session.commit()
        return jsonify(pData), 201

@main_routes.route('/pokemon/<string:pokemon_name>', methods=['GET', 'DELETE'])
def pokemon_handler(pokemon_name):
    if request.method == 'GET':
        try: 
            foundPoke = Pokemon.query.filter_by(name=str(pokemon_name)).first()
            output = {"name": foundPoke.name, "frontImg": foundPoke.frontImg, "move1":foundPoke.move1}
            return output
        except:
            raise exceptions.BadRequest(f"We do not have a pokemon with that id: {pokemon_name}")
    elif request.method == 'DELETE':
        try:
            foundPoke = Pokemon.query.filter_by(name=str(pokemon_name)).first()
            db.session.delete(foundPoke)
            db.session.commit()
            return "deleted", 204
        except:
            raise exceptions.BadRequest(f"failed to delete pokemon with htat id: {pokemon_name}")
