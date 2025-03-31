# basics/hello_world.py

# A simple function that prints "Hello, World!" when called
def simple_hello():
    # print() is used to show output on the screen
    print("Hello, World!")

# Another function that uses a variable to store the message
def hello_with_variable():
    # We store the text "Hello, World!" in a variable called message
    message = "Hello, World!"
    # Then we print the value of that variable
    print(message)

# A function that takes a name as input and prints a personalized message
def hello_with_name(name):
    # f-strings help us insert variables into strings easily
    print(f"Hello, {name}!")

# This part only runs when you run this file directly (not when you import it from another file)
if __name__ == "__main__":
    # Calling each function one by one
    simple_hello()               # Output: Hello, World!
    hello_with_variable()        # Output: Hello, World!
    hello_with_name("Tashy")     # Output: Hello, Tashy!
