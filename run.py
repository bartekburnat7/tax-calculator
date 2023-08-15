def tax_calculate(x):
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


def main():
    print("-------------------------------------------")
    print("    WELCOME TO THE TAX CALCULATOR (UK)")
    print("APPLICATION THAT CALCULATES YOUR ANNUAL TAX")
    print("-------------------------------------------")
    user_name = input("Please enter your Name: ")
    while True:
        user_earn = input("How much you earn a year: £")

        try:
            float()
            user_earn = float(user_earn)
            print(user_name , ", you would be paying: £" , "%.2f" % tax_calculate(user_earn) , "per year")
        except ValueError:
            if user_earn.isnumeric():
                user_earn = int(user_earn)
                print(user_name , ", you would be paying: £", "%.2f" % tax_calculate(user_earn) , "per year")
            else:
                print("Insert a correct value to calculate your annual Tax!!!")
main()