# Initialize an empty list to store pizza toppings
toppings = []

# Prompt the user to enter pizza toppings
print("Enter pizza toppings. Enter 'quit' when you're finished.")

while True:
    topping = input("Enter a topping: ").lower()  # Convert the input to lowercase
    if topping == 'quit':
        break  # Exit the loop if the user enters 'quit'
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)

# Print the list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print(topping.capitalize())
