# Define a list of sandwich orders
sandwich_orders = ['tuna', 'ham and cheese', 'turkey', 'BLT', 'roast beef']

# Define an empty list to store finished sandwiches
finished_sandwiches = []

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
