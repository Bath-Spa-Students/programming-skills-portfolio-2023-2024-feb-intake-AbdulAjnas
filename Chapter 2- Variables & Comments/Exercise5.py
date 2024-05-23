# Define the cost of each USB stick and the total budget
usb_stick_cost = 6  # in pounds
total_budget = 50   # in pounds

# Calculate the maximum number of USB sticks she can buy
num_usb_sticks = total_budget // usb_stick_cost

# Calculate the remaining pounds after buying USB sticks
remaining_pounds = total_budget % usb_stick_cost

# Print the results
print(f"The girl can buy {num_usb_sticks} USB sticks and will have £{remaining_pounds} left.")
