
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

initial_menu_list = ["1. Calculator. ", "2. Tell me a joke!", "3. Tell me a fun fact!", "4. Exit Program"]

print("Welcome to Tim Sywulka ChatBot v0.01!")

def get_user_name():
    return input("For starters, what is your name?: ")

def get_user_age(user_name1):
    return input(f"Nice to meet you {user_name1}, what is your age?: ")

def main_list1():
    print("Please pick an option below to proceed:\n")
    for item in initial_menu_list:
        print(item);

    while True:
        user_choice = int(input("\nPlease enter what pathway you wish to go (ex: 1, 2, etc): "))
        if user_choice >= 1 and user_choice <= 4:
            print(f"You wish to proceed with pathway {user_choice}.")
            break
        else:
            print("Opps! It seems like you didnt enter an integer!")

    return user_choice

def check_if_exit(user_input_pathway):
    if user_input_pathway == 4:
        return True
    else:
        return False





def main():


    user_name = get_user_name()
    user_age = get_user_age(user_name)
    print(f"Really cool that you are {user_age}, anybody can code at any age!")
    user_pathway = main_list1()
    did_user_exit = check_if_exit(user_pathway)
    if did_user_exit:
        print("Goodbye. Come again later!")





if __name__ == "__main__":
    main()
