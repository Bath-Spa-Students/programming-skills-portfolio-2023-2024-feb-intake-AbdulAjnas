# Define a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ['tuna', 'pastrami', 'ham and cheese', 'pastrami', 'turkey', 'BLT', 'pastrami', 'roast beef', 'pastrami']

# Define an empty list to store finished sandwiches
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    # Take the first sandwich order from the list
    current_order = sandwich_orders.pop(0)
    
    # Make the sandwich and print a message
    print(f"I made your {current_order} sandwich.")
    
    # Move the made sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
