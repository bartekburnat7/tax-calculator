# This function takes the input from "user_earn"
# and checks which tax band the user would qualify
# in and then calculates the tax accordingly.
def calculate(user_earnings):
    print("\nCalculating....\n")
    if user_earnings <= 12570:
        print("--- Personal Allowance Band ---")
        tax_payable = 0
    elif user_earnings >= 12571 and user_earnings <= 50270:
        print("--- Basic rate Band ---")
        tax_payable = 0.2 * (user_earnings - 12570)
    elif user_earnings >= 50271 and user_earnings <= 125140:
        print("--- Higher rate Band ---")
        tax_payable = 7540 + 0.4 * (user_earnings - 50270)
    elif user_earnings > 125140:
        print("--- Additional rate Band ---")
        tax_payable = (7540 + 29948) + 0.45 * (user_earnings - 125140)
    return tax_payable


# Prints welcome message at the start of the program
def print_welcome_msg():
    print("-------------------------------------------")
    print("    WELCOME TO THE TAX CALCULATOR (UK)")
    print("APPLICATION THAT CALCULATES YOUR ANNUAL TAX")
    print("-------------------------------------------")


# Takes user name and runs validations
def take_user_name_input():
    name = input("Please enter your Name: ")
    if len(name) > 2 and name.replace(" ", "").isalpha():
        return name
    else:
        print("The name you entered is invalid. Enter a valid \n")
        return take_user_name_input()


# Main loop for the application which
# takes the user input and displays the
# amount of tax you would need to pay.
def main():
    print_welcome_msg()

    name = take_user_name_input()

    while True:
        text_one = ", you would be paying: £"
        text_two = "TAX this year"
        user_earnings = input("How much you earn a year: £")
        # This is an input handler. If the value is a float or
        # a numerical number it will accept it. But if it has alphabets
        # or special character has been entered then the
        # application would not accept it and return an error message.
        try:
            user_earnings = float(user_earnings)
            if user_earnings < 0:
                raise ValueError
            tax_payable = calculate(user_earnings)
            print(name, text_one, "%.2f" % tax_payable, text_two)
        except ValueError:
            print("Insert a correct value to calculate your annual Tax!!!")


main()
