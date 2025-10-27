# Large shirt function with default size
def make_shirt(message, size="large"):
    """Display the size and message of the T-shirt."""
    print(f"Making a {size} T-shirt with the message: '{message}'")

# Calling the function with a custom size
make_shirt("Python is awesome!", "medium")

# Calling the function with the default size
make_shirt("I love coding!")
