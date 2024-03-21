# DESCRIPTION: A program for the One Stop Insurance Company to enter and calculate insurance policy information to its new customers.
# AUTHOR: Brian Janes
# DATE: March 17th, 2024

# Import the required libraries
import datetime
import FormatValues as FV
import sys
import time
import string
# I am importing the os library to clear the screen after the user is done entering a customer's information. I don't like the way the terminal can look once it's filled with used inputs!
import os

# Trying to use ANSII escape codes to format text in the terminal.
# Define ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m'
GREEN = "\033[32m"

# Define program constants
# Defining valid provinces.
PROVINCES = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS',
             'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT']
# Defining valid payment methods.
VALID_PAYMENT_METHODS = ['FULL', 'MONTHLY', 'DOWN PAY']

POLICY_NUM = 1944
BASIC_PREM_COST = 869.00
XTRA_CAR_DISCOUNT_RATE = .25
XTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_COST = 58.00
HST_RATE = .15
MONTHLY_PRCSSING_FEE = 39.99

current_time = datetime.datetime.now()
current_hour = current_time.hour
time_of_day = FV.time_of_day(current_hour)

# Define the allowed characters for the address, and city inputs.
ALLOWED_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,'-1234567890"

# Main Program
# This clears up the terminal of the couple of lines related to the file before starting.
os.system('cls' if os.name == 'nt' else 'clear')
while True:
    # User information inputs.
    print()
    print()
    print("                 Welcome to One Stop Insurance Group!")
    print("   Before we get started, we need to collect some infomation from you.")
    print("=========================================================================")
    print()
    print()
    # User name inputs.
    # First name - just a simple check to make sure the user only enters alphabetic characters.
    while True:
        first_name = input("Enter the customer's first name: ").strip()
        if not first_name.isalpha():
            print(
                f"{RED}Data Entry Error - First name must contain only alphabetic characters. Please try again.{RESET}")
            continue
        else:
            break

    # Last name - just a simple check to make sure the user only enters alphabetic characters.
    while True:
        print()
        last_name = input("Enter the customer's last name:  ").strip()
        if not last_name.isalpha():
            print(
                f"{RED}Data Entry Error - Last name must contain only alphabetic characters. Please try again.{RESET}")
            continue
        else:
            break

    # Formatting customer's full name.
    full_name = first_name.title() + " " + last_name.title()

    # Pausing the program for 3 seconds to allow the user to read the information.
    print()
    print()
    for _ in range(2):  # Change to control number of 'blinks'
        print(f'{GREEN}    Processing Policy Information...{RESET}', end='\r')
        time.sleep(.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)

    # Cleaning up the terminal for the user to move to address inputs.
    os.system('cls' if os.name == 'nt' else 'clear')
    # User address input.
    print()
    print()
    # Greeting the user with their previously entered name based on the time of day.
    print(f"               Good {time_of_day}, {full_name}!")
    print("   We are excited to offer you a new insurance policy today.")
    print("         Let's move on to your address information.")
    print("==============================================================")
    print()
    print()
    while True:
        address = input("Enter the customer's address: ").title()
        if not all(char in ALLOWED_CHARACTERS for char in address):
            print()
            print(
                f"{RED}Data Entry Error - Invalid address. Please try again.{RESET}")
            continue
        else:
            break

    # User city input.
    while True:
        print()
        city = string.capwords(input("Enter the customer's city: "))
        if not all(char in ALLOWED_CHARACTERS for char in city):
            print()
            print(
                f"{RED}Data Entry Error - Invalid character used. Please try again.{RESET}")
            continue
        else:
            break

    # Province input.
    while True:
        print()
        province = input(
            "Enter the customer's province (2 letter abbreviation): ")
        validated_province = FV.validate_province(province)
        if validated_province is None:
            print()
            print(
                f"{RED}Data Entry Error - Please enter a valid province abbreviation.{RESET}")
            continue
        else:
            province = validated_province
            break

    # Postal code input - Explained in FormatValues.py
    while True:
        print()
        postal_code = input("Enter the customer's postal code (X#X#X#): ")
        check_post_code = FV.check_postal_code(postal_code)
        if check_post_code == "Data Entry Error (Invalid postal code) - Postal code must be 6 characters long. Please try again." or check_post_code == "Data Entry Error (Invalid postal code) - Postal code must have letters in the first, third, and fifth positions. Please try again." or check_post_code == "Data Entry Error (Invalid postal code) - Postal code must have digits in the second, fourth, and sixth positions. Please try again.":
            print()
            print(f"{RED} + {check_post_code} + {RESET}")
            continue
        else:
            postal_code = check_post_code
            break

    # Phone number input - Explained in FormatValues.py.
    while True:
        print()
        phone_number = input(
            "Enter the customer's phone number (##########): ")
        # Check if the phone number is valid length, and all digits, return an error message if it's not & return the formatted phone number if it is.
        check_phone_num = FV.check_phone_num(phone_number)
        if check_phone_num == "Data Entry Error (Invalid phone number) - Character count issue. Please try again." or check_phone_num == "Data Entry Error (Invalid phone number) - Phone number must only be numerical values. Please try again.":
            print()
            print(f"{RED} + {check_phone_num} + {RESET}")
            continue
        else:
            phone_number = check_phone_num
            break

    formatted_extra_car_discount_rate = "{:.0f}%".format(
        XTRA_CAR_DISCOUNT_RATE * 100)

    # Pausing the program for 3 seconds to allow the user to read the information.
    print()
    print()
    for _ in range(3):  # Change to control number of 'blinks'
        print(f"{GREEN}    Processing Policy Information...{RESET}", end='\r')
        time.sleep(.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)

    # Insurance policy information inputs.
    # Clearing the terminal before a new section of inputs.
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print()
    print(f"            Don't worry {full_name}, we're almost done!")
    print("         Let's move on to your insurance policy information.          ")
    print("======================================================================")
    print()
    print()
    while True:
        try:
            num_cars_insured = int(
                input("Enter the number of cars to be insured: "))
            print()
            # Check if the number of cars insured is less than 1, return an error message if it is.
            if num_cars_insured < 1:
                print()
                print(
                    RED + "Data Entry Error - Number of cars insured cannot be less than 1. Please try again." + RESET)
                continue
            elif num_cars_insured > 1:
                print(f"{GREEN}You have entered {num_cars_insured} cars to be insured. This qualifies you for a {formatted_extra_car_discount_rate} discount!{RESET}")
                print()
                break
            elif num_cars_insured == 1:
                print(
                    f"{RED}You have entered {num_cars_insured} vehicle to be insured.")
                add_another_vehicle = input(
                    f"Would you like to add another vehicle to qualify for a {formatted_extra_car_discount_rate} discount? (Y/N): ").upper()
                print()
                if add_another_vehicle == "Y":
                    print()
                    print(
                        f"{GREEN}You have chosen to add another vehicle. This qualifies you for a {formatted_extra_car_discount_rate} discount!{RESET}")
                    print()
                    num_cars_insured += 1
                    break
                elif add_another_vehicle == "N":
                    print(f"{GREEN}You have chosen to insure only {num_cars_insured} car.\nIf you wish to review your policy in the future,\nFeel free to contact us at One Stop Insurance Group.{RESET}")
                    print()
                    print("One Stop Insurance Group")
                    print("Customer Service: 1-800-555-5555")
                    print()
                    break
                else:
                    print()
                    print(f"{RED}Invalid input. Please enter Y or N.{RESET}")
                    continue
        except ValueError:
            print()
            print(
                f"{RED}Data Entry Error - Number of cars insured must be a valid integer. Please try again.{RESET}")

    # Extra liability input
    while True:
        extra_liability = input(
            "Would you like to add extra liability coverage? (Y/N): ").upper()
        if extra_liability == "Y":
            # Display 'Yes' if the user enters 'Y'
            extra_liability_display = "Yes"
            # Adding a coloured confirmation message to the user.
            print(
                f"{GREEN}Added liability coverage up to $1,000,000 to your policy.{RESET}")
            print()
            break
        elif extra_liability == "N":
            # Display 'No' if the user enters 'N'
            extra_liability_display = "No"
            # Adding a coloured confirmation message to the user.
            print(f"{RED}No extra liability coverage added to your policy.{RESET}")
            print()
            break
        else:
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}")
            continue

    # Glass coverage input
    while True:
        glass_coverage = input(
            "Would you like to add glass coverage? (Y/N):           ").upper()
        if glass_coverage == "Y":
            # Display 'Yes' if the user enters 'Y'.
            glass_coverage_display = "Yes"
            # Adding a confirmation message to the user.
            print(f"{GREEN}Added Glass coverage to your policy.{RESET}")
            print()
            break
        elif glass_coverage == "N":
            # Display 'No' if the user enters 'N'.
            glass_coverage_display = "No"
            # Adding a confirmation message to the user.
            print(f"{RED}No glass coverage added to your policy.{RESET}")
            print()
            break
        else:
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}")
            continue

    # Loaner car coverage input
    while True:
        loaner_car = input(
            "Would you like to add loaner car coverage? (Y/N):      ").upper()
        if loaner_car == "Y":
            # Display 'Yes' if the user enters 'Y'.
            loaner_car_display = "Yes"
            # Adding a confirmation message to the user.
            print(f"{GREEN}Added Loaner car coverage to your policy.{RESET}")
            print()
            break
        elif loaner_car == "N":
            # Display 'No' if the user enters 'N'.
            loaner_car_display = "No"
            # Adding a confirmation message to the user.
            print(f"{RED}No loaner car coverage added to your policy.{RESET}")
            print()
            break
        else:
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}")
            continue

    # Pausing the program for 3 seconds to allow the user to read the information.
    print()
    print()
    for _ in range(3):  # Change to control number of 'blinks'
        print(f"{GREEN}    Processing Policy Information...{RESET}", end='\r')
        time.sleep(.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)

    # Processing for policy information.
    # Calculate insurance premium for the first automobile.
    insurance_premium = BASIC_PREM_COST

    # Calculate discount for additional automobiles.
    if num_cars_insured > 1:
        insurance_premium += (num_cars_insured - 1) * \
            (BASIC_PREM_COST * XTRA_CAR_DISCOUNT_RATE)

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

    # Calculate total cost. I have to perform this calculation here so that I can properly validate my downpayment amount.
    total_cost = total_insurance_premium + hst_cost

    # Payment method input
    # I chose to do this after some amount of processing so that I could vailidate the down payment amount against the total cost. The downpayment can't be greater than total cost!
    while True:
        # Initialize down payment to 0.
        down_payment = 0
        payment_method = input(
            "Enter the payment method (Full, Monthly, or Down Pay): ").title()

        # Check if the payment method is valid by cross-referencing with the list of valid payment methods.
        while payment_method.upper() not in VALID_PAYMENT_METHODS:
            print()
            print(
                f"{RED}Data Entry Error - Invalid payment method. Please enter a valid payment method.{RESET}")
            payment_method = input(
                "Enter the payment method (Full, Monthly, or Down Pay): ").title()

        # If the payment method is 'Down Pay', ask the user to enter the down payment amount.
        if payment_method.upper() == 'DOWN PAY':
            while True:
                try:
                    # Ask the user to enter the down payment amount.
                    print()
                    down_payment = float(
                        input("Enter the amount of the down payment: $"))
                    # Check if the down payment is valid.
                    if down_payment <= 0:
                        print()
                        print(
                            f"{RED}Data Entry Error - Down payment cannot be less than or equal to 0. Please try again.{RESET}")
                        continue
                    # Here is where I am having issues. I need to check if the down payment is greater than the total cost, and return an error message if it is.
                    if down_payment > total_cost:
                        print()
                        print(
                            f"{RED}Data Entry Error - Down payment cannot be greater than the total cost. Please try again.{RESET}")
                        continue
                    print()
                    print(
                        f"{GREEN}You have chosen our Down Payment option. {RESET}")
                    print()
                    break
                except ValueError:
                    print()
                    print(
                        f"{RED}Data Entry Error - Invalid input. Please enter a valid numerical value.{RESET}")
            break
        elif payment_method.upper() == 'FULL' or payment_method.upper() == 'MONTHLY':
            if payment_method.upper() == 'FULL':
                print()
                print(f"{GREEN}You have chosen our Full payment option. {RESET}")
                print()
            elif payment_method.upper() == 'MONTHLY':
                print()
                print(f"{GREEN}You have chosen our Monthly payment option. {RESET}")
                print()
            break

    # Pausing the program for 3 seconds to allow the user to read the information.
    print()
    print()
    for _ in range(3):  # Change to control number of 'blinks'
        print(f"{GREEN}    Processing Policy Information...{RESET}", end='\r')
        time.sleep(.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)

    # Claims information inputs.
    # Create empty list to store claim information.
    claims = []

    # Loop to allow user to enter claim information.
    while True:
        # Clearing the terminal before claims are input.
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print()
        print("                  Last Section - We promise!                 ")
        print("           Let's finish up with claim information.           ")
        print("==============================================================")
        print()
        print()
        claim_number = input(
            "Enter the claim number (#####) (type 'DONE' to finish): ")
        if claim_number.upper() == 'DONE':
            break
        else:
            # Check if the claim number is 5 characters long, return an error message if it's not.
            if len(claim_number) != 5:
                print()
                print(
                    f"{RED}Data Entry Error - Invalid claim number. Please enter a 5-digit number.{RESET}")
                continue
            # Check if the claim number is a valid number, return an error message if it's not.
            elif not claim_number.isdigit():
                print()
                print(
                    f"{RED}Data Entry Error - Invalid claim number. Please enter a numerical value.{RESET}")
                continue

        while True:
            claim_date = input("Enter the claim date (YYYY-MM-DD): ")
            validated_date = FV.check_date(claim_date)
            if validated_date != "Data Entry Error (Invalid date) - Date must be in the format YYYY-MM-DD.":
                break
            else:
                print()
                print(f"{RED} + {validated_date} + {RESET}")

        while True:
            try:
                claim_amount = float(input("Enter the claim amount: "))
                # Check if the claim amount is greater than 0, return an error message if it's not.
                if claim_amount <= 0:
                    print()
                    print(
                        f"{RED}Data Entry Error - Claim amount must be greater than 0. Please try again.{RESET}")
                    continue
                break
            except ValueError:
                print()
                print(
                    f"{RED}Data Entry Error - Invalid input. Please enter a valid numerical value.{RESET}")

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
        if repeat.upper() == 'Y':
            continue
        elif repeat.upper() == 'N':
            if os.name == 'nt':  # If the system is Windows
                os.system('cls')
            else:
                os.system('clear')
            break
        else:
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}")

    # Procesing for payment type, invoice date, and premium cost (pre-tax)
    # Calculate monthly payment.
    if payment_method.upper() == 'FULL':
        monthly_payment = total_cost / 8
    elif payment_method.upper() == 'MONTHLY':
        monthly_payment = (total_cost + MONTHLY_PRCSSING_FEE) / 8
    elif payment_method.upper() == 'DOWN PAY':
        monthly_payment = (total_cost - down_payment +
                           MONTHLY_PRCSSING_FEE) / 8

    # Calculate total insurance premium (pre-tax)
    total_insurance_premium_pretax = insurance_premium + extra_costs

    # Calculate invoice date and first payment date.
    invoice_date = datetime.datetime.now().strftime('%Y-%m-%d')
    first_payment_date = (datetime.datetime.now(
    ) + datetime.timedelta(days=30)).replace(day=1).strftime('%Y-%m-%d')

    # Formatting
    # Formatting dollar values + other misc formatting.
    formatted_down_payment = FV.FDollar2(down_payment)
    formatted_insurance_premium = FV.FDollar2(insurance_premium)
    formatted_hst_cost = FV.FDollar2(hst_cost)
    formatted_total_cost = FV.FDollar2(total_cost)
    formatted_monthly_payment = FV.FDollar2(monthly_payment)
    formatted_extra_costs = FV.FDollar2(extra_costs)
    formatted_pre_tax = FV.FDollar2(total_insurance_premium_pretax)

    print()
    print()
    for _ in range(4):
        print(f"{GREEN}        PROCESSING YOUR RECEIPT{RESET}", end='\r')
        time.sleep(.3)
        # Flush the output buffer to make sure the message is displayed immediately
        sys.stdout.flush()
        time.sleep(0.3)
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)

    # Display receipt.
    print()
    print("============================================")
    print()
    print("             One Stop Insurance")
    print("         Policy Information Receipt")
    print()
    print("============================================")
    print()
    print(f"      Policy Number:           {POLICY_NUM:>6d}")
    print(f"      Invoice Date:           {invoice_date:<10s}")
    print()
    print("============================================")
    print()
    print(f"    Name:                  {full_name:<22s}")
    print(f"    Address:               {address:<20s}")
    print(f"    City:                  {city:<18s}")
    print(f"    Province:              {province:<2s}")
    print(f"    Postal Code:           {postal_code:<7s}")
    print(f"    Phone Number:          {phone_number:<14s}")
    print()
    print("============================================")
    print()
    print(f"    Number of Cars Insured:            {num_cars_insured:>2d}")
    print(
        f"    Extra Liability Coverage:         {extra_liability_display:<3s}")
    print(
        f"    Glass Coverage:                   {glass_coverage_display:<3s}")
    print(f"    Loaner Car Coverage:              {loaner_car_display:<3s}")
    print()
    # Formatting this string to the right for better consistent alignment.
    print(f"    Payment Method:              {payment_method:>8s}")
    # Display Down Payment if payment method is 'Down Pay'.
    if payment_method.upper() == 'DOWN PAY':
        print(f"    Down Payment:              {formatted_down_payment:>10s}")
    # Display Calculated Values
    print()
    print(f"    Insurance Premium:         {formatted_insurance_premium:>10s}")
    print(f"    Extra Costs Total:         {formatted_extra_costs:>10s}")
    print(f"    HST:                       {formatted_hst_cost:>10s}")
    print(f"    Total Cost:                {formatted_total_cost:>10s}")
    print(f"    Monthly Payment:           {formatted_monthly_payment:>10s}")
    print()
    print(f"    First Payment Date:        {first_payment_date:>10s}")
    print()

    # Display claims information after receipt.
    print("============================================")
    print()
    if len(claims) == 0:
        print(f"              No previous claims.")
        print()
    else:
        print(f"      Claim #   Claim Date      Amount")
        print(f"      --------------------------------")
    for claim in claims:
        print()
        print(
            f"      {claim['claim_number']}     {claim['claim_date']}  {claim['claim_amount']:>10s}")
        print()
    print(f"      --------------------------------")

    # Display total insurance premium (pre-tax) and save policy data message
    print()
    print(f"      Premium Cost(Pre-tax):{formatted_pre_tax:>10s}")
    print()

    for _ in range(5):  # Change to control number of 'blinks'
        print("          Saving claim data...", end='\r')
        time.sleep(.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write('\033[2K\r')
        time.sleep(.3)
    print()
    print(GREEN + "      Policy data - successfully saved", end='\r' + RESET)
    print()

    # Increment the policy number by 1.
    POLICY_NUM += 1

    # Housekeeping
    # Ask the user if they want to enter another customer
    print()
    while True:
        repeat = input(
            f"{RED}Do you want to enter another customer? (Y/N): {RESET}").upper()
        print()
        if repeat == 'Y':
            if os.name == 'nt':  # If the system is Windows
                os.system('cls')
            else:
                os.system('clear')
            break
        elif repeat == 'N':
            if os.name == 'nt':  # If the system is Windows
                os.system('cls')
            else:
                os.system('clear')
            print()
            print(f"{GREEN}Thank you for using One Stop Insurance Group!{RESET}")
            exit()
        else:
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}")
