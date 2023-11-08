# This function takes the input from "user_earn"
# and checks which tax band the user would qualify
# in and then calculates the tax accordingly.
def calculate(x):
    print("\nCalculating....\n")
    if x <= 12570:
        print("--- Personal Allowance Band ---")
        tax_pay = 0
        return tax_pay

    elif x >= 12571 and x <= 50270:
        print("--- Basic rate Band ---")
        tax_pay = 0.2 * (x - 12570)
        return tax_pay

    elif x >= 50271 and x <= 125140:
        print("--- Higher rate Band ---")
        tax_pay = 7540 + 0.4 * (x - 50270)
        return tax_pay

    elif x > 125140:
        print("--- Additional rate Band ---")
        tax_pay = (7540 + 29948) + 0.45 * (x - 125140)
        return tax_pay

# Main loop for the application which
# takes the user input and displays the
# amount of tax you would need to pay.


def main():
    print("-------------------------------------------")
    print("    WELCOME TO THE TAX CALCULATOR (UK)")
    print("APPLICATION THAT CALCULATES YOUR ANNUAL TAX")
    print("-------------------------------------------")

    name = input("Please enter your Name: ")
    text_one = ", you would be paying: £"
    text_two = "TAX this year"
    while True:
        user_earn = input("How much you earn a year: £")
        # This is an input handler. If the value is a float or
        # a numerical number it will accept it. But if a letter
        # or special character has been entered then the
        # application would not accept it and return an error message.
        try:
            float()
            user_earn = float(user_earn)
            print(name, text_one, "%.2f" % calculate(user_earn), text_two)
        except ValueError:
            if user_earn.isnumeric():
                user_earn = int(user_earn)
                print(name, text_one, "%.2f" % calculate(user_earn), text_two)
            else:
                print("Insert a correct value to calculate your annual Tax!!!")


main()
