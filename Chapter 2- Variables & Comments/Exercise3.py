# Define the person's name with whitespace characters
name = "\t  John Doe \n"

# Print the name with whitespace around it
print("Name with whitespace:")
print(name)

# Print the name using each stripping function
print("\nStripping Functions:")
print("Using lstrip():", name.lstrip())
print("Using rstrip():", name.rstrip())
print("Using strip():", name.strip())
