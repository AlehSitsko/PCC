# T-Shirt function
def make_shirt(size, message):
    """Display the size and message of the T-shirt."""
    print(f"Making a {size} T-shirt with the message: '{message}'")

# Calling the function with positional arguments
make_shirt("large", "I love Python!")

# Calling the function with keyword arguments
make_shirt(message="Coding is fun!", size="medium")
