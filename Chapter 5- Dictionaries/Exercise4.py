# Define a dictionary containing major rivers and the countries they run through
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Print a sentence about each river using a loop
print("Sentences about each river:")
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country}.")

# Print the name of each river included in the dictionary using a loop
print("\nNames of rivers:")
for river in rivers.keys():
    print(river.capitalize())

# Print the name of each country included in the dictionary using a loop
print("\nNames of countries:")
for country in rivers.values()
    print(country)
