# Define ticket prices based on age
ticket_prices = {
    '3 or younger': 0,
    'between 3 and 12': 10,
    'over 12': 15
}

# Loop to ask users their age and determine ticket price
while True:
    age = input("Enter your age (or 'quit' to exit): ")
    
    if age.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    age = int(age)  # Convert the input to an integer
    
    # Determine ticket price based on age
    if age <= 3:
        print("Your movie ticket is free!")
    elif age <= 12:
        print(f"Your movie ticket costs ${ticket_prices['between 3 and 12']}.")
    else:
        print(f"Your movie ticket costs ${ticket_prices['over 12']}.")
