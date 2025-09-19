

initial_menu_list = ["1. Calculator. ", "2. FAQ.", "3. How to Donate.", "4. Exit Program"]

print("Welcome to Tim Sywulka ChatBot v0.01!")

def get_user_name():
    return input("For starters, what is your name?: ")

def get_user_age(user_name1):
    user_age = int(input(f"Nice to meet you {user_name1}, what is your age?: "))
    if user_age < 18:
        out_string = "You are not an adult yet! Almost there!"
        return out_string
    if 24 >= user_age >= 18:
        out_string = "You are Gen Z, you are destined for Greatness!"
        return out_string
    if 64 >= user_age > 24:
        out_string = "You are almost at retirement, you will get there someday."
        return out_string
    if user_age > 64:
        out_string = "Retirement is here!"
        return out_string

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
    loop = True
    while loop:
        user_name = get_user_name()
        user_age_string = get_user_age(user_name)
        print(user_age_string)
        user_pathway = main_list1()
        did_user_exit = check_if_exit(user_pathway)

        print("\n\n\n")
        if did_user_exit:
            print("Goodbye. Come again later!")
            loop = False





if __name__ == "__main__":
    main()
