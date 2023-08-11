def tax_calculate(x):
    print("Calculating....")
    if x <= 12570:
        tax_pay = 0
        return tax_pay

    elif x >= 12571 and x <= 50270:
        tax_pay = 0.2 * (x - 12570)
        return tax_pay

    elif x >= 50271 and x <= 125140:
        tax_pay = 7539.8 + 0.4 * (x - 50271)
        return tax_pay

    elif x > 125140:
        tax_pay = 29947.6 + 0.45 * (x - 125140)
        return tax_pay

def main():
    user_name = input("Enter your Name: ")
    user_earn = input("How much you earn a year: £")

main()