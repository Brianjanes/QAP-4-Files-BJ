# DESCRIPTION: A program for the One Stop Insurance Company to enter and calculate insurance policy information to its new customers.
# AUTHOR: Brian Janes
# DATE: March 17th, 2024

# Import the required libraries
import datetime
import FormatValues as FV
import sys
import time
import string

# Define program constants
# Defining valid provinces.
PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
# Defining valid payment methods.
VALID_PAYMENT_METHODS = ['FULL', 'MONTHLY', 'DOWN PAY']

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

# Define the allowed characters for the address, and city inputs.
ALLOWED_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .'-1234567890"

# Main Program
print()
while True:
    # User information inputs.
    print()
    # User name inputs.
    first_name = input("Enter the customer's first name: ").title()
    last_name =  input("Enter the customer's last name:  ").title()

    # User address input.
    print()
    while True:
        address = input("Enter the customer's address: ").title()
        if not all(char in ALLOWED_CHARACTERS for char in address):
            print("Data Entry Error - Invalid address. Please try again.")
            continue
        else:
            break

    # User city input.
    while True:
        city = string.capwords(input("Enter the customer's city: "))
        if not all(char in ALLOWED_CHARACTERS for char in city):
            print("Data Entry Error - Invalid city. Please try again.")
            continue
        else:
            break

    # Province input.
    while True:
        province = input("Enter the customer's province (2 letter abbreviation): ").upper()
        if province not in PROVINCES:
            print("Data Entry Error - Invalid province abbreviation. Please try again.")
            continue
        else:
            break

    # Postal code input - Explained in FormatValues.py
    while True:
        postal_code = input("Enter the customer's postal code (X#X#X#): ")
        check_post_code = FV.check_postal_code(postal_code)
        if check_post_code == "Data Entry Error - Invalid postal code. Please try again.":
            print(check_post_code)
            continue
        else:
            postal_code = check_post_code
            break

    # Phone number input - Explained in FormatValues.py.
    while True:
        print()
        phone_number = input("Enter the customer's phone number (##########): ")
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
            num_cars_insured = int(input("Enter the number of cars to be insured: "))
            print()
            # Check if the number of cars insured is less than 1, return an error message if it is.
            if num_cars_insured < 1:
                print("Data Entry Error - Number of cars insured cannot be less than 1. Please try again.")
                continue
            else:
                break
        except ValueError:
            print("Data Entry Error - Number of cars insured must be a valid integer. Please try again.")

    # Extra liability input
    while True:
        extra_liability = input("Would you like to add extra liability coverage? (Y/N): ").upper()
        if extra_liability == "Y" or extra_liability == "N":
            # Display 'Yes' if the user enters 'Y', and 'No' if the user enters 'N'.
            extra_liability_display = "Yes" if extra_liability == "Y" else "No"
            break
        else:
            print("Data Entry Error - Invalid input. Please enter 'Y' or 'N'.")
            continue

    # Glass coverage input
    while True:
        glass_coverage = input("Would you like to add glass coverage? (Y/N):           ").upper()
        if glass_coverage == "Y" or glass_coverage == "N":
            # Display 'Yes' if the user enters 'Y', and 'No' if the user enters 'N'.
            glass_coverage_display = "Yes" if glass_coverage == "Y" else "No"
            break
        else:
            print("Data Entry Error - Invalid input. Please enter 'Y' or 'N'.")
            continue

    # Loaner car coverage input
    while True:
        loaner_car = input("Would you like to add loaner car coverage? (Y/N):      ").upper()
        if loaner_car == "Y" or loaner_car == "N":
            # Display 'Yes' if the user enters 'Y', and 'No' if the user enters 'N'.
            loaner_car_display = "Yes" if loaner_car == "Y" else "No"
            break
        else:
            print("Data Entry Error - Invalid input. Please enter 'Y' or 'N'.")
            continue
    
    # Payment method input
    while True:
        down_payment = 0
        print()
        payment_method = input("Enter the payment method (Full, Monthly, Down Pay): ").title()

        # Check if the payment method is valid cross referencing out already created list of valid payment methods, return an error message if it's not.
        while payment_method.upper() not in VALID_PAYMENT_METHODS:
            print("Data Entry Error - Invalid payment method. Please enter a valid payment method.")
            break
        
        # If the payment method is 'Down Pay', ask the user to enter the down payment amount.
        if payment_method.upper() == 'DOWN PAY':
            while True:
                try:
                    # Ask the user to enter the down payment amount. Cannot be less than or equal to 0.
                    down_payment = float(input("Enter the amount of the down payment: "))
                    if down_payment <= 0:
                        print("Data Entry Error - Down payment cannot be less than or equal to 0. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Data Entry Error - Invalid input. Please enter a valid numerical value.")
        break
    
    # Create empty list to store claim information.
    claims = []

    # Loop to allow user to enter claim information.
    while True:
        print()
        claim_number = input("Enter the claim number (#####) (type 'DONE' to finish): ")
        if claim_number.upper() == 'DONE':
            break
        else:
            # Check if the claim number is 5 characters long, return an error message if it's not.
            if len(claim_number) != 5:
                print("Data Entry Error - Invalid claim number. Please enter a 5-digit number.")
                continue
            # Check if the claim number is a valid number, return an error message if it's not.
            elif not claim_number.isdigit():
                print("Data Entry Error - Invalid claim number. Please enter a numerical value.")
                continue
            else:
                pass

        # Deciding not to validate this input.
        claim_date = input("Enter the claim date (YYYY-MM-DD): ")


        while True:
            try:
                claim_amount = float(input("Enter the claim amount: "))
                # Check if the claim amount is greater than 0, return an error message if it's not.
                if claim_amount <= 0:
                    print("Data Entry Error - Claim amount must be greater than 0. Please try again.")
                    continue
                break
            except ValueError:
                print("Data Entry Error - Invalid input. Please enter a valid numerical value.")

        # Format the claim amount to a dollar value.
        formatted_claim_amount = FV.FDollar2(claim_amount)

        # Creating a claims dictionary to store the individual claim information.
        current_claim = {
            'claim_number': claim_number,
            'claim_date': claim_date,
            'claim_amount': formatted_claim_amount
        }

        # Appending the current claim to the claims list.
        claims.append(current_claim)

        # Ask the user if they want to enter another customer.
        print()
        repeat = input("Do you want to enter another claim? (Y/N): ")
        if repeat.upper() != 'Y':
            break

    # Processing 
    
    # Calculate insurance premium for the first automobile.
    insurance_premium = BASIC_PREM_COST

    # Calculate discount for additional automobiles.
    if num_cars_insured > 1:
        insurance_premium += (num_cars_insured - 1) * (BASIC_PREM_COST * XTRA_CAR_DISCOUNT_RATE)

    # Calculate extra costs for additional options.
    extra_costs = 0
    if extra_liability == 'Y':
        extra_costs += num_cars_insured * XTRA_LIABILITY_COST
    if glass_coverage == 'Y':
        extra_costs += num_cars_insured * GLASS_COVERAGE_COST
    if loaner_car == 'Y':
        extra_costs += num_cars_insured * LOANER_COST

    # Calculate total insurance premium.
    total_insurance_premium = insurance_premium + extra_costs

    # Calculate HST.
    hst_cost = total_insurance_premium * HST_RATE

    # Calculate total cost.
    total_cost = total_insurance_premium + hst_cost

    # Calculate monthly payment.
    if payment_method.upper() == 'FULL':
        monthly_payment = total_cost / 8
    elif payment_method.upper() == 'MONTHLY':
        monthly_payment = (total_cost + MONTHLY_PRCSSING_FEE) / 8
    elif payment_method.upper() == 'DOWN PAY':
        monthly_payment = (total_cost - down_payment + MONTHLY_PRCSSING_FEE) / 8

    # Calculate invoice date and first payment date.
    invoice_date = datetime.datetime.now().strftime('%Y-%m-%d')
    first_payment_date = (datetime.datetime.now() + datetime.timedelta(days=30)).replace(day=1).strftime('%Y-%m-%d')

    # Formatting dollar values + other misc formatting.
    formatted_down_payment = FV.FDollar2(down_payment)
    formatted_insurance_premium = FV.FDollar2(insurance_premium)
    formatted_hst_cost = FV.FDollar2(hst_cost)
    formatted_total_cost = FV.FDollar2(total_cost)
    formatted_monthly_payment = FV.FDollar2(monthly_payment)
    # Formatting customer's full name.
    full_name = first_name + " " + last_name


    # Display receipt.
    print()
    print("==============================================")
    print("              One Stop Insurance              ")
    print("          Policy Information Receipt          ")
    print("==============================================")

    # Display Customer Information
    print()
    print(f"  Name:                     {full_name:<22s}")
    print(f"  Address:                  {address:<20s}")
    print(f"  City:                     {city:<18s}")
    print(f"  Province:                 {province:<2s}")
    print(f"  Postal Code:              {postal_code:<7s}")
    print(f"  Phone Number:             {phone_number:<14s}")

    # Display Insurance Policy Information
    print()
    print(f"  Number of Cars Insured:   {num_cars_insured:>2d}")
    print(f"  Extra Liability Coverage:  {extra_liability_display:<3s}")
    print(f"  Glass Coverage:            {glass_coverage_display:<3s}")
    print(f"  Loaner Car Coverage:       {loaner_car_display:<3s}")
    print(f"  Payment Method:           {payment_method:<8s}")

    # Display Down Payment if payment method is 'Down Pay'.
    if payment_method.upper() == 'DOWN PAY':
        print(f"  Down Payment:           {formatted_down_payment:>10s}")

    # Display Calculated Values
    print()
    print(f"  Insurance Premium:      {formatted_insurance_premium:>10s}")
    print(f"  HST:                    {formatted_hst_cost:>10s}")
    print(f"  Total Cost:             {formatted_total_cost:>10s}")
    print(f"  Monthly Payment:        {formatted_monthly_payment:>10s}")
    print()

    # Display claims information
    print(f"  -----------------------------------")
    print()
    print(f"   Previous Claims:")
    print()
    print(f"   Claim #    Claim Date      Amount")
    print(f"  -----------------------------------")
    for claim in claims:
        print(f"   {claim['claim_number']}      {claim['claim_date']}  {claim['claim_amount']:>10s}")
    print(f"  -----------------------------------")

    # Calculate total insurance premium (pre-tax)
    total_insurance_premium_pretax = insurance_premium + extra_costs
    formatted_pre_tax = FV.FDollar2(total_insurance_premium_pretax)

    # Display total insurance premium (pre-tax) and save policy data message
    print()
    print(f"  Premium Cost (Pre-tax): {formatted_pre_tax:>10s}")
    print()

    for _ in range(5):  # Change to control number of 'blinks'
        print('Saving claim data...', end='\r')
        time.sleep(.3)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(.3)

    print()
    print("Policy data successfully saved.", end='\r')
    print()

    # Housekeeping
    # Increase the next policy number by 1
    POLICY_NUM += 1

    # Ask the user if they want to enter another customer
    print()
    repeat = input("Do you want to enter another customer? (Y/N): ")
    if repeat.upper() != 'Y':
        break
    else:
        continue
