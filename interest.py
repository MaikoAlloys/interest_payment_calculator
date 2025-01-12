def main():
    print("This is an interest calculator")
    print("")

    principal=float(input("Enter the loan amount: "))
    apr=float(input("Input the annual interest rate: "))
    years=int(input("Input amount of years: "))

    monthly_interest_rate=apr/12
    amount_of_months=years*12
    monthly_payment=principal*monthly_interest_rate/(1-(1+monthly_interest_rate))**(amount_of_months)

    print("Your monthly payment is "+ str(monthly_payment))

main()
