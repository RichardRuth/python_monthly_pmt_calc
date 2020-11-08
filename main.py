#!/usr/bin/env python3

#COP2002.0M1 Programming Logic
#Module 9 Project 9-1 Monthly Payment Calculator Program
#Submitted by Richard Ruth

# Program obtains loan amount, yearly interest rate, and term data from user, and calculates and displays monthly payment amount
# Note: Per project rubrics, it is assumed that user will enter valid data

from decimal import Decimal
from decimal import ROUND_HALF_UP #used because business math is calculated in this program
import locale as lc

def main():

    # Main module obtains user loan data, calls monthly payment function for calculation, and displays monthly payment output

    print("\nMonthly Payment Calculator\n")
    choice = "y"
    while choice.lower() == "y":

        # Get user data and convert to Decimal and int values
        
        print("DATA ENTRY")
        loan_amount = Decimal(input("Loan amount:           "))
        yearly_interest = Decimal(input("Yearly interest rate:  "))
        yearly_interest = yearly_interest.quantize(Decimal("1.0"), ROUND_HALF_UP) # in case user enters interest rate beyond 1 decimal place
        years = int(input("Years:                 "))

        # Call monthly payment calculation function
        
        monthly_payment = get_monthly_payment(loan_amount, yearly_interest, years)
        print()

        # Format and display output data

        result = lc.setlocale(lc.LC_ALL, "")
        if result == "C":
            lc.setlocale(lc.LC_ALL, "en_US")
        print("FORMATTED RESULTS")
        print("{:25} {:>12}".format("Loan amount:", lc.currency(loan_amount, grouping=True)))
        print("{:25} {:>12.1%}".format("Yearly interest rate:", yearly_interest / 100))
        print("{:25} {:>12d}".format("Number of years:", years))
        print("{:25} {:>12}".format("Monthly payment:", lc.currency(monthly_payment, grouping=True)), "\n")

        choice = input("Continue? (y/n): ")
        print()
        
# Function get_monthly_payment calculates monthly payment amount using user entered loan data

def get_monthly_payment(loan_amount, yearly_interest, years):
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12
    monthly_payment = Decimal("0.00")
    monthly_payment = loan_amount * monthly_interest_rate / (1-1/(1 + monthly_interest_rate) ** months)
    monthly_payment = monthly_payment.quantize(Decimal("1.00"), ROUND_HALF_UP)
    return monthly_payment

# If this module is the main module, call the main() function

if __name__ == "__main__":
     main()
