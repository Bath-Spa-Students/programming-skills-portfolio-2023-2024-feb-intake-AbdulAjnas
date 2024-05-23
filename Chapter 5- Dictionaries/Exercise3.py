# Define a dictionary to represent a glossary of programming terms
glossary = {
    'variable': 'A container for storing data value.',
    'function': 'A block of organized, reusable code that performs a specific task.',
    'loop': 'A programming construct that repeats a block of code until a certain condition is met.',
    'list': 'A collection of items that are ordered and changeable. Allows duplicate members.',
    'dictionary': 'A collection of key-value pairs, where each key maps to a value.',
    'tuple': 'A collection of ordered and immutable elements.',
    'set': 'A collection of unique elements with no duplicate members.',
    'method': 'A function that is associated with an object and can be called on that object.',
    'class': 'A blueprint for creating objects, providing initial values and behaviors.',
    'module': 'A file containing Python code that can be imported and used in another Python script.'
}

# Print each word and its meaning with a loop
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:")
    print(meaning)
    print()  # Print a blank line after each word-meaning pair
