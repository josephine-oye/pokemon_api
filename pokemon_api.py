import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
print('Enter your pokemon:')

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(choice)
response = requests.get(url)
player_data = json.loads(response.text)

# to get ability
abilities = player_data['abilities'][0]
ability = abilities['ability']

# to format height and weight properly
height = int(player_data['height'])
weight = int(player_data['weight'])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print('Name: {}'.format(player_data['name']))
print('Weight: {}'.format(weight_formatted) + "(kgs)")
print('Height: {}'.format(height_formatted) + "(m)")
print('Ability: {}'.format(ability['name']))

# CPU gets a random Pokemon
cpu_choice = random.choice(pokemon_list)['name']

# Get the CPU Pokemon's data from the API
cpu_url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(cpu_choice)
response = requests.get(cpu_url)
cpu_data = json.loads(response.text)

# To get ability
cpu_abilities = cpu_data['abilities'][0]
cpu_ability = cpu_abilities['ability']

# Format height and weight properly
cpu_height = int(cpu_data['height'])
cpu_weight = int(cpu_data['weight'])

cpu_height_formatted = cpu_height / 10
cpu_weight_formatted = cpu_weight / 10

# Print the CPU pokemon's data
print('\nCPU POKÉMON')
print('Name: {}'.format(cpu_data['name']))
print('Weight: {}'.format(cpu_weight_formatted) + "(kgs)")
print('Height: {}'.format(cpu_height_formatted) + "(m)")
print('Ability: {}'.format(cpu_ability['name']))

def get_stats(pokemon_data):
    stats = pokemon_data["stats"]

    hp = stats[0]["base_stat"]
    attack = stats[1]["base_stat"]
    defense = stats[2]["base_stat"]

    return hp, attack, defense
