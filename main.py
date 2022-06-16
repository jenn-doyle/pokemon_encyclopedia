import requests
import random

pokemon_ids = random.sample(range(1, 152), 6)
# print(pokemon_ids)

for pokemon_id in pokemon_ids:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    # Converts from JavaScript Object Notation into Python lists and dictionaries
    pokemon_data = response.json()

    # print(pokemon_data['id'])
    # print(pokemon_data['name'])

    print(f"You got Pokemon number {pokemon_data['id']}, their name is {pokemon_data['name'].capitalize()}!")
    print(f"Height: {pokemon_data['height']} • Weight: {pokemon_data['weight']}")

    pokemon_types = []
    for type_data in pokemon_data['types']:
        pokemon_types.append(type_data['type']['name'])

    print(f"Type(s): {' and '.join(pokemon_types)}")

    pokemon_abilities = []
    for ability_data in pokemon_data['abilities']:
        pokemon_abilities.append(ability_data['ability']['name'])

    print(f"Abilities: {', '.join(pokemon_abilities)}")
    print()
