def make_shirt(size, message):
    """Prints a summary of the shirt size and message."""
    print(f"A {size}-sized shirt will be made with the message: '{message}'.")

# Call the function using positional arguments
make_shirt("medium", "Keep coding!")

# Call the function using keyword arguments
make_shirt(size="large", message="Python Rocks!")
