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

def calculate_damage(attack, defense):
    # attack = attack // 2
    damage = attack - (defense // 2)  # damage formula
    return max(1, damage)             # damage cannot be zero or negative

# Get stats for player and CPU using your function
player_hp, player_attack, player_defense = get_stats(player_data)
cpu_hp, cpu_attack, cpu_defense = get_stats(cpu_data)

print(" ")

turn = 0

while player_hp > 0 and cpu_hp > 0:

    turn += 1
    print("\nTurn number", turn, "\n")

    # Player attacks CPU
    damage = calculate_damage(player_attack, cpu_defense)
    cpu_hp -= damage
    print(f"{player_data['name']} hits {cpu_data['name']} for {damage}!")
    print(f"{cpu_data['name']} HP: {cpu_hp}")

    # CPU attacks Player
    damage = calculate_damage(cpu_attack, player_defense)
    player_hp -= damage
    print(f"{cpu_data['name']} hits {player_data['name']} for {damage}!")
    print(f"{player_data['name']} HP: {player_hp}")


if player_hp <= 0:
    print("You lost.")
elif player_hp <= 0 and cpu_hp <= 0:
    print("It's a tie.")
else:
    print("You win!")
