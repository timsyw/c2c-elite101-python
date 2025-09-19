
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


print("Welcome to Tim Sywulka ChatBot v0.01!")

def get_user_name():
    return input("For starters, what is your name?: ")

def get_user_age(user_name1):
    return input(f"Nice to meet you {user_name1}, what is your age?: ")



def main():


    user_name = get_user_name()
    user_age = get_user_age(user_name)
    


if __name__ == "__main__":
    main()
