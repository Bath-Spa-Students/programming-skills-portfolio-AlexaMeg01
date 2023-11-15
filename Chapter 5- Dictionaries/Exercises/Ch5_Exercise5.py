# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {'animal type': 'DOg(yorkie)',
    'name': 'Luna',
    'owner': 'Alexa',
    'weight': '3.6',
    'eats': 'Dog Food',}

pets.append(pet)

pet = {'animal type': 'Cat',
    'name': 'Mandy',
    'owner': 'Andy',
    'weight': '9',
    'eats': 'seeds',}

pets.append(pet)

pet = {'animal type' : 'Fish',
    'name' : 'goldy',
    'owner': 'Elay',
    'weight': '0.2' ,
    'eats': 'fishfood'}

pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
