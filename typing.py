import random

def generate_random_string2(length):
    """Generates a random string of the specified length using the given characters."""

    characters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_string(length):
    """Generates a random string of the specified length using the given characters."""
    
    characters = "!@#$%^&*()`~-=_+[]{}\|;:'\",<.>/?"

    return ''.join(random.choice(characters) for _ in range(length))

def assess_accuracy(random_string, user_input):
    """Compares the user's input to the random string and assesses accuracy."""
    if user_input == random_string:
        print("Congratulations! Your input is correct.")
    else:
        print("Incorrect. The correct string was:", random_string)

while True:
    random_string_length = 30
    random_string = generate_random_string(random_string_length)
    print("Type the following random string:")
    print(random_string)

    user_input = input("Enter your input or press q to quit: ")
    if(user_input == 'q'):
        break
    assess_accuracy(random_string, user_input)
