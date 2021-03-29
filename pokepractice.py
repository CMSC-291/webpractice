import json

import requests

poke_name = input("Give me a pokemon name")

url = "https://pokeapi.co/api/v2/pokemon/{}".format(poke_name)

pokedex = requests.get(url).json()
print(json.dumps(pokedex, indent=2))
print("That pokemon weighs {} [whatever unit they use in PokeWorld]".format(pokedex['weight']))
print("it has abilities:")
for ability in pokedex['abilities']:
    print(ability['ability']['name'])