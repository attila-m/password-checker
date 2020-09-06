password = "How should I know?"

def password_checker(password_input, trial_count): 
    if password_input == password:
        print("You are in.")
    elif password_input == "quit":
        exit()
    elif trial_count >= 5:
        print("You are out.")
        exit()
    else:
        password_input = raw_input("No, try again.\nWhat is the password? ")
        password_checker(password_input, trial_count + 1)

password_input = raw_input("What is the password? ")
password_checker(password_input, 1)
