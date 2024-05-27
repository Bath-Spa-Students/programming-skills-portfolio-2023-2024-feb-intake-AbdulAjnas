# Create dictionaries representing different pets
pet1 = {'animal': 'dog', 'owner': 'Alice'}
pet2 = {'animal': 'cat', 'owner': 'Bob'}
pet3 = {'animal': 'rabbit', 'owner': 'Charlie'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop through the list and print everything known about each pet
for pet in pets:
    print(f"Animal: {pet['animal'].capitalize()}")
    print(f"Owner: {pet['owner'].capitalize()}")
    print()  # Print a blank line after each pet's information
