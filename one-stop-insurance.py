# DESCRIPTION: A program for the One Stop Insurance Company to enter and calculate insurance policy information to its new customers.
# AUTHOR: Brian Janes
# DATE: March 17th, 2024

# Import the required libraries
import datetime
import FormatValues as FV
import sys
import time

# Define program constants
# Defining valid provinces.
PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
# Defining valid payment methods.
VALID_PAYMENT_METHODS = ['Full', 'Monthly', 'Down Pay']

# Open the defaults file and read the values into variables
# f = open('Default.dat', 'r')
# POLICY_NUM = int(f.readline())
# BASIC_PREM_COST = float(f.readline())
# XTRA_CAR_DISCOUNT_RATE = float(f.readline())
# XTRA_LIABILITY_COST = float(f.readline())
# GLASS_COVERAGE_COST = float(f.readline())
# LOANER_COST = float(f.readline())
# HST_RATE = float(f.readline())
# MONTHLY_PRCSSING_FEE = float(f.readline())
# f.close()

POLICY_NUM = 1944
BASIC_PREM_COST = 869.00
XTRA_CAR_DISCOUNT_RATE = .25
XTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_COST = 58.00
HST_RATE = .15
MONTHLY_PRCSSING_FEE = 39.99

# Main Program
print()
while True:
    # User information inputs
    print()
    first_name = "brian" # input("Enter the customer's first name: ").title()
    last_name = "janes" # input("Enter the customer's last name: ").title()

    # User address inputs
    print()
    address = "123 main st." # input("Enter the customer's address: ").title()
    city = "st johns" # input("Enter the customer's city: ").title()

    while True:
        province = input("Enter the customer's province (2 letter abbreviation): ").upper()
        # Check if the province is valid
        if province not in PROVINCES:
            print("Data Entry Error - Invalid province abbreviation. Please try again.")
            continue
        else:
            break

    while True:
        postal_code = input("Enter the customer's postal code (X#X#X#): ")
            # Check if the postal code is valid, return an error message if it's not & return the formatted postal code if it is.
        check_post_code = FV.check_postal_code(postal_code)
        if check_post_code == "Data Entry Error - Invalid postal code. Please try again.":
            print(check_post_code)
            continue
        else:
            postal_code = check_post_code
            break

    while True:
        print()
        phone_number = "7091234234" # input("Enter the customer's phone number (##########): ")
        # Check if the phone number is valid length, and all digits, return an error message if it's not & return the formatted phone number if it is.
        check_phone_num = FV.check_phone_num(phone_number)
        if check_phone_num == "Data Entry Error - Invalid phone number. Please try again.":
            print(check_phone_num)
            continue
        else:
            phone_number = check_phone_num
            break
    
    # Insurance policy information inputs.
    print()
    while True:
        try:
            num_cars_insured = 2 # int(input("Enter the number of cars to be insured: "))
            if num_cars_insured < 1:
                print("Data Entry Error - Number of cars insured cannot be less than 1. Please try again.")
                continue
            else:
                break
        except:
            print("Data Entry Error - Number of cars insured must be a valid integer. Please try again.")

    while True:
        extra_liability = input("Would you like to add extra liability coverage? (Up to $1, 000, 000) (Y/N): ").upper()
        if extra_liability == "Y" or extra_liability == "N":
            break
        else:
            print("Data Entry Error - Invalid input. Please enter 'Y' or 'N'.")
            continue

    glass_coverage = input("Would you like to add glass coverage? (Y/N): ").upper()

    loaner_car = input("Would you like to add loaner car coverage? (Y/N): ").upper()

    while True:
        down_payment = 0
        print()
        payment_method = input("Enter the payment method (Full, Monthly, Down Pay): ").title()

        while payment_method not in VALID_PAYMENT_METHODS:
            print("Data Entry Error - Invalid payment method. Please enter a valid payment method.")
            break

        if payment_method.upper() == 'DOWN PAY':
            down_payment = float(input("Enter the amount of the down payment: "))
            if down_payment <= 0:
                print("Data Entry Error - Down payment cannot be less than 0. Please try again.")
                continue
        break
    
# PAYMENT METHOD CURRENTLY CAUSING ERROR - STEPPING AWAY

    # Create empty lists to store claim information
    claim_numbers = []
    claim_dates = []
    claim_amounts = []

    # Loop to allow user to enter claim information
    while True:
        print()
        claim_number = "12345" # input("Enter the claim number (#####) (type 'DONE' to finish): ")
        if claim_number.upper() == 'DONE':
            break
        
        claim_date = "2024-01-01" # input("Enter the claim date (YYYY-MM-DD): ")
        claim_amount = 1288.01 # float(input("Enter the claim amount: "))

        # Append claim information to respective lists
        claim_numbers.append(claim_number)
        claim_dates.append(claim_date)
        claim_amounts.append(claim_amount)

        # Ask the user if they want to enter another customer
        print()
        repeat = input("Do you want to enter another claim? (Y/N): ")
        if repeat.upper() != 'Y':
            break

    # Processing 
    
    # Calculate insurance premium for the first automobile
    insurance_premium = BASIC_PREM_COST

    # Calculate discount for additional automobiles
    if num_cars_insured > 1:
        insurance_premium += (num_cars_insured - 1) * (BASIC_PREM_COST * XTRA_CAR_DISCOUNT_RATE)

    # Calculate extra costs for additional options
    extra_costs = 0
    if extra_liability == 'Y':
        extra_costs += num_cars_insured * XTRA_LIABILITY_DISCOUNT
    if glass_coverage == 'Y':
        extra_costs += num_cars_insured * GLASS_COVERAGE_COST
    if loaner_car == 'Y':
        extra_costs += num_cars_insured * LOANER_COST

    # Calculate total insurance premium
    total_insurance_premium = insurance_premium + extra_costs

    # Calculate HST
    hst_cost = total_insurance_premium * HST_RATE

    # Calculate total cost
    total_cost = total_insurance_premium + hst_cost

    # Calculate monthly payment
    if payment_method.upper() == 'FULL':
        monthly_payment = total_cost / 8
    elif payment_method.upper() == 'MONTHLY':
        monthly_payment = (total_cost + MONTHLY_PRCSSING_FEE) / 8
    elif payment_method.upper() == 'DOWN PAY':
        monthly_payment = (total_cost - down_payment + MONTHLY_PRCSSING_FEE) / 8

    # Calculate invoice date and first payment date
    invoice_date = datetime.datetime.now().strftime('%Y-%m-%d')
    first_payment_date = (datetime.datetime.now() + datetime.timedelta(days=30)).replace(day=1).strftime('%Y-%m-%d')

    print("\nPrevious Claims:")
    print()
    print("   Claim #    Claim Date      Amount")
    print("  -----------------------------------")
    for i in range(len(claim_numbers)):
        print(f"   {claim_numbers[i]}      {claim_dates[i]}   {FV.FDollar2(claim_amounts[i])}")