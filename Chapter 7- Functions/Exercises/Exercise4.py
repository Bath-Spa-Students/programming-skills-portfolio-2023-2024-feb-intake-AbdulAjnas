def make_shirt(size="large", message="I love Python"):
    """Prints a summary of the shirt size and message."""
    print(f"A {size}-sized shirt will be made with the message: '{message}'.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a small shirt with a different message
make_shirt(size="small", message="Keep coding!")
