# User Authentication

# Username validation function

def validate_username(username):

    if username.endswith("@gmail.com"):

        return True

    elif username.endswith("@pccoepune.org"):

        first_name = username.split("@")[0]

        if "." in first_name:

            return True

    return False

# Password validation function

def validate_password(password):

    if len(password) >= 6 and len(password) <= 12:

        has_special_char = False

        has_capital_letter = False

        has_digit = False

        for char in password:

            if char in "!@#$%^&*()":

                has_special_char = True

            elif char.isupper():

                has_capital_letter = True

            elif char.isdigit():

                has_digit = True

        if has_special_char and has_capital_letter and has_digit:

            return True

    return False

# Main program

print("-- User Authentication --")

username = input("Enter your username: ")

password = input("Enter your password: ")

if validate_username(username):

    if validate_password(password):

        print("Authentication successful!")

    else:

        print("Invalid password.")

else:

    print("Invalid username.")
