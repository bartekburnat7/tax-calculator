def tax_calculate(x):
    print("Calculating....")
    if x <= 12570:
        tax_pay = 0
        return tax_pay

    elif x >= 12571 and x <= 50270:
        tax_pay = 0.2 * (x - 12570)
        return tax_pay

    elif x >= 50271 and x <= 125140:
        tax_pay = 7540 + 0.4 * (x - 50270)
        return tax_pay

    elif x > 125140:
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
            print(tax_calculate(user_earn))
        except ValueError:
            if user_earn.isnumeric():
                user_earn = int(user_earn)
                print(tax_calculate(user_earn))
            else:
                print("Insert a correct value to calculate your annual Tax!!!")    
main()

