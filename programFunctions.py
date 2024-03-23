# Importing required modules.
import os
import FormatValues as FV
import string
import time
import sys
import datetime

current_time = datetime.datetime.now()
current_hour = current_time.hour
current_date = current_time.date()

# Define allowed characters for user inputs.
ALLOWED_CHARACTERS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,'-1234567890"
)

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"


def clear_terminal():
    """
    Function to clear the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")


def processing_blinker():
    """
    A short blinking statement to pause inbetween inputs to create a better flow for the user.
    """
    print()
    # Change to control number of 'blinks'
    for _ in range(2):
        print(f"{GREEN}    Processing Policy Information...{RESET}", end="\r")
        # Pause for 0.3 seconds
        time.sleep(0.3)
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)


def saving_blinker():
    # Change to control number of 'blinks'
    for _ in range(5):
        print("          Saving claim data...", end="\r")
        # Pause for 0.3 seconds
        time.sleep(0.3)
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)
    print()
    print(f"{GREEN}      Policy data - successfully saved{RESET}", end="\r")
    print()


def receipt_blinker():
    print()
    print()
    # Change to control number of 'blinks'
    for _ in range(4):
        print(f"{GREEN}        PROCESSING YOUR RECEIPT{RESET}", end="\r")
        # Pause for 0.3 seconds
        time.sleep(0.3)
        # Flush the output buffer to make sure the message is displayed immediately
        sys.stdout.flush()
        time.sleep(0.3)
        # Clears the entire line and carriage returns
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)


def time_of_day(current_hour):
    """
    Accepts a time in 24-hour format

    Returns the time of day as morning, afternoon, or evening.
    """
    # Define the time ranges for morning, afternoon, and night
    # 6:00 AM to 11:59 AM
    morning_range = range(6, 12)
    # 12:00 PM to 5:59 PM
    afternoon_range = range(12, 18)
    # 6:00 PM to 11:59 PM
    night_range = range(18, 24)

    # Determine whether it's morning, afternoon, or night
    if current_hour in morning_range:
        return "morning"
    elif current_hour in afternoon_range:
        return "afternoon"
    elif current_hour in night_range:
        return "evening"
    return "night"


def get_customer_full_name():
    """
    Function calls for user input of first and last name.

    Returns the customer's full name.
    """
    # First name input - strip the strong and check for only alphabetic characters.
    # User information inputs.
    print()
    print()
    print("                 Welcome to One Stop Insurance Group!")
    print("   Before we get started, we need to collect some infomation from you.")
    print("=========================================================================")
    print()
    print()
    while True:
        first_name = input("  Enter the customer's first name: ").strip()
        if not first_name.isalpha():
            print()
            print(
                f"{RED}Data Entry Error - First name must contain only alphabetic characters. Please try again.{RESET}")
            print()
            continue
        break

    # Last name input - strip the strong and check for only alphabetic characters.
    while True:
        print()
        last_name = input("  Enter the customer's last name:  ").strip()
        if not last_name.isalpha():
            print()
            print(
                f"{RED}Data Entry Error - Last name must contain only alphabetic characters. Please try again.{RESET}"
            )
            continue

        break
    # Blinking message to simulate processing, followed by clearing the terminal to increase readability.
    processing_blinker()
    clear_terminal()
    # Concatenating and formatting the customer's full name for return.
    return first_name.title() + " " + last_name.title()


def get_customer_info(full_name):
    """
    Function displays a personalized greeting to the user, calls for them to input street address, city, province, postal code, and phone number.

    Returns the customer's address, city, province, postal code, and phone number.
    """
    time = time_of_day(current_hour)
    print()
    print()
    print(f"                   Good {time}, {full_name}!")
    print("        We are excited to offer you a new insurance policy today.")
    print("               Let's move on to your address information.                ")
    print("=========================================================================")
    print()
    print()
    # User address input.
    while True:
        address = input("  Enter the customer's address: ").title()
        # Using isspace() to check if the string is only whitespace.
        if address.isspace() or address == "":
            print()
            print(
                f"{RED}Data Entry Error - Address cannot be blank. Please try again.{RESET}"
            )
            print()
            continue
        elif not all(char in ALLOWED_CHARACTERS for char in address):
            print()
            print(
                f"{RED}Data Entry Error - Invalid address. Please try again.{RESET}")
            print()
            continue
        break

    # User city input.
    while True:
        print()
        city = string.capwords(input("  Enter the customer's city: "))
        if city.isspace() or city == "":
            print()
            print(
                f"{RED}Data Entry Error - City cannot be blank. Please try again.{RESET}"
            )
            continue
        elif not all(char in ALLOWED_CHARACTERS for char in city):
            print()
            print(
                f"{RED}Data Entry Error - Invalid character used. Please try again.{RESET}"
            )
            continue
        break

    # Province input.
    while True:
        print()
        province = input(
            "  Enter the customer's province (2 letter abbreviation): ")
        validated_province = FV.validate_province(province)
        if province.isspace() or province == "":
            print()
            print(
                f"{RED}Data Entry Error - Province cannot be blank. Please try again.{RESET}"
            )
            continue
        if not validated_province:
            print()
            print(
                f"{RED}Data Entry Error - Please enter a valid province abbreviation.{RESET}"
            )
            continue
        province = validated_province
        break

    # Postal code input - Explained in FormatValues.py
    while True:
        print()
        postal_code = input("  Enter the customer's postal code (X#X#X#): ")
        check_post_code = FV.check_postal_code(postal_code)
        if postal_code.isspace() or postal_code == "":
            print()
            print(
                f"{RED}Data Entry Error - Postal code cannot be blank. Please try again.{RESET}")
            continue
        elif check_post_code.startswith("Data Entry Error"):
            print()
            print(f"{RED}{check_post_code}{RESET}")
            continue
        postal_code = check_post_code
        break

    # Phone number input - Explained in FormatValues.py.
    while True:
        print()
        phone_number = input(
            "  Enter the customer's phone number (##########): ")
        # Check if the phone number is valid length, and all digits, return an error message if it's not & return the formatted phone number if it is.
        validated_phone_num = FV.check_phone_num(phone_number)
        if len(validated_phone_num) != 14:
            print()
            print(f"{RED}{validated_phone_num}{RESET}")
            continue
        phone_number = validated_phone_num
        break
    # Blinking message to simulate processing, followed by clearing the terminal to increase readability.
    processing_blinker()
    clear_terminal()
    # Return the validated and formatted address, city, province, postal code, and phone number.
    return address, city, province, postal_code, phone_number


def get_insurance_info(full_name):
    """
    Function calls for user input of the number of cars to be insured, 

    Returns the number of cars to be insured, extra liability coverage, glass coverage, and loaner car coverage.
    """
    print()
    print()
    print(f"              Don't worry {full_name}, we're almost done!")
    print("           Let's move on to your insurance policy information.           ")
    print("=========================================================================")
    print()
    print()

    while True:
        try:
            num_cars_insured = int(
                input("  Enter the number of cars to be insured: "))
            if num_cars_insured < 1 or num_cars_insured > 9:
                print()
                print(
                    f"{RED}Data Entry Error - Number of cars insured cannot be less than 1 or greater than 9. Please try again.{RESET}")
                print()
                continue  # Continue the loop if input is less than 1
            elif num_cars_insured == 1:
                print()
                print(
                    f"{RED}You have entered {num_cars_insured} vehicle to be insured.{RESET}")
                print()
                add_another_vehicle = input(
                    "  Would you like to add another vehicle? (Y/N): ").upper()
                if add_another_vehicle == "Y":
                    num_cars_insured += 1
                elif add_another_vehicle == "N":
                    print()
                    print(
                        f"{GREEN}You have chosen to insure only {num_cars_insured} car.")
                    print()
                    print(
                        f"If you wish to review your policy in the future, feel free to contact us at One Stop Insurance Group.")
                    print()
                    print(f"    One Stop Insurance Group")
                    print(f"    Customer Service: 1-800-555-5555{RESET}")
                    print()
                    break  # Break out of the loop if 'N' is entered
                print(f"{RED}Invalid input. Please enter Y or N.{RESET}")
            print()
            print(
                f"{GREEN}You have entered {num_cars_insured} cars to be insured.{RESET}")
            print()
            break
        except ValueError:
            print(
                f"{RED}Data Entry Error - Number of cars insured must be a valid integer. Please try again.{RESET}")

    while True:
        extra_liability = input(
            "  Would you like to add extra liability coverage? (Y/N): ").upper()
        if extra_liability not in ['Y', 'N']:
            print()
            print(f"{RED}Invalid input. Please enter 'Y' or 'N'.{RESET}")
            continue

        extra_liability_display = "Yes" if extra_liability == "Y" else "No"
        if extra_liability == "Yes" or extra_liability == "Y":
            print()
            print(
                f"{GREEN}Extra liability coverage: {extra_liability_display}{RESET}")
            print()
        elif extra_liability == "No" or extra_liability == "N":
            print()
            print(
                f"{RED}Extra liability coverage: {extra_liability_display}{RESET}")
            print()
        break

    while True:
        glass_coverage = input(
            "  Would you like to add glass coverage? (Y/N): ").upper()
        if glass_coverage not in ['Y', 'N']:
            print()
            print(f"{RED}Invalid input. Please enter 'Y' or 'N'.{RESET}")
            print()
            continue

        glass_coverage_display = "Yes" if glass_coverage == "Y" else "No"
        if glass_coverage == "Yes" or glass_coverage == "Y":
            print()
            print(
                f"{GREEN}Glass coverage: {glass_coverage_display}{RESET}")
            print()
        elif glass_coverage == "No" or glass_coverage == "N":
            print()
            print(
                f"{RED}Glass coverage: {glass_coverage_display}{RESET}")
            print()
        break

    while True:
        loaner_car = input(
            "  Would you like to add loaner car coverage? (Y/N): ").upper()
        if loaner_car not in ['Y', 'N']:
            print()
            print(f"{RED}Invalid input. Please enter 'Y' or 'N'.{RESET}")
            print()

        loaner_car_display = "Yes" if loaner_car == "Y" else "No"
        if loaner_car == "Yes" or loaner_car == "Y":
            print()
            print(
                f"{GREEN}Loaner car coverage: {loaner_car_display}{RESET}")
            print()
        elif loaner_car == "No" or loaner_car == "N":
            print()
            print(
                f"{RED}Loaner car coverage: {loaner_car_display}{RESET}")
            print()
        break

    # Blinking message to simulate processing, followed by clearing the terminal to increase readability.
    processing_blinker()
    clear_terminal()
    return num_cars_insured, extra_liability_display, glass_coverage_display, loaner_car_display


def get_payment_method(full_name, total_cost, processing_fee):
    """
    Accepts the total cost of the policy to validate against the potential down payment amount.

    Returns the payment method and if necessary the down payment amount.
    """
    VALID_PAYMENT_METHODS = ["FULL", "MONTHLY", "DOWN PAY", "F", "M", "D"]
    down_payment_amt = 0

    print()
    print()
    print(f"                       Almost there {full_name}!")
    print("                   Let's get your payment information.")
    print("=========================================================================")
    print()
    print()
    while True:
        print(f"{GREEN}    You can use F, M, or D for short.{RESET}")
        print()
        payment_method = input(
            "  Enter the payment method (Full, Monthly, or Down Pay): ").upper()
        if payment_method not in VALID_PAYMENT_METHODS:
            print()
            print(
                f"{RED}Data Entry Error - Invalid payment method. Please enter a valid payment method.{RESET}")
            print()
            continue

        elif payment_method == "DOWN PAY" or payment_method == "D":
            print()
            print(f"{GREEN}You have chosen the Down Payment option. {RESET}")
            while True:
                try:
                    print()
                    down_payment_amt = float(
                        input(f"{GREEN}  Enter the amount of the down payment: {RESET}"))
                    if down_payment_amt <= 0:
                        print()
                        print(
                            f"{RED}Data Entry Error - Down payment cannot be less than or equal to 0. Please try again.{RESET}")
                        continue
                    elif down_payment_amt > total_cost:
                        print()
                        print(
                            f"{RED}Data Entry Error - Down payment cannot be greater than the total cost. Please try again.{RESET}")
                        continue
                    break
                except ValueError:
                    print()
                    print(
                        f"{RED}Data Entry Error - Invalid input. {ValueError}.{RESET}")

        elif payment_method in {"FULL", "F", "MONTHLY", "M"}:
            payment_method = "Full" if payment_method in {
                "FULL", "F"} else "Monthly"
            print()
            print(
                f"{GREEN}You have chosen the {payment_method} payment option. {RESET}")

        monthly_payment = 0
        # Calculate monthly payment.
        if payment_method == "Monthly" or payment_method == "M":
            monthly_payment = (total_cost + processing_fee) / 8
        elif payment_method == "Down Pay" or payment_method == "D":
            monthly_payment = (
                total_cost - down_payment_amt + processing_fee) / 8

        # Before returning, replace short forms with full names (I thought I was doing this but it doesn't seem to be working as exected).
        if payment_method == "F":
            payment_method = "Full"
        elif payment_method == "M":
            payment_method = "Monthly"
        elif payment_method == "D":
            payment_method = "Down Pay"

        # Format the monthly payment as a dollar amount.
        monthly_payment = FV.FDollar2(monthly_payment)
        payment_method = payment_method.title()
        # Blinking message to simulate processing, followed by clearing the terminal to increase readability.
        processing_blinker()
        clear_terminal()
        return payment_method, down_payment_amt, monthly_payment


def get_claims():
    """
    Function to get claim information from the user. Loops over 3 inputs: claim number, claim date, and claim amount. The user can choose to enter no claims, or multiple claims. 

    Returns a list of dictionaries, where each dictionary represents a claim.
    """
    claims = []

    print()
    print()
    print("                        Last Section - We promise!")
    print("                 Let's finish up with claim information.")
    print("=========================================================================")
    print()
    print()

    while True:
        while True:
            claim_number = input(
                "  Enter the claim number (#####) (type 'DONE' to finish): ")
            if claim_number.isspace() or claim_number == "":
                print()
                print(
                    f"{RED}Data Entry Error - Claim number cannot be empty. Please try again.{RESET}")
                print()
                continue
            elif claim_number.upper() == "DONE":
                break
            elif claim_number.isdigit() and len(claim_number) == 5:
                break
            print()
            print(
                f"{RED}Data Entry Error - Invalid claim number. Please enter 5 numerical digits.{RESET}")
            print()
        if claim_number.upper() == "DONE":
            break

        while True:
            print()
            # Remove leading and trailing spaces
            claim_date = input("  Enter the claim date (YYYY-MM-DD): ").strip()
            validated_date = FV.check_date(claim_date)

            # Check if the input is empty or just spaces
            if not claim_date or claim_date.isspace():
                print()
                print(
                    f"{RED}Data Entry Error - Claim date cannot be empty. Please enter a valid date in the format YYYY-MM-DD.{RESET}")
                continue
            elif validated_date.startswith("Data Entry Error"):
                print()
                print(f"{RED}{validated_date}{RESET}")
                continue
            else:
                # Check if the claim date is within the last 10 years
                claim_date_age_limit = datetime.datetime.strptime(
                    claim_date, "%Y-%m-%d").date()
                ten_years_ago = current_date.replace(
                    year=current_date.year - 10)
                if not claim_date_age_limit >= ten_years_ago:
                    print()
                    print(
                        f"{RED}Data Entry Error - Claim date cannot be more than 10 years old. Please try again.{RESET}")
                    continue
                break

        while True:
            try:
                print()
                # Remove leading and trailing spaces
                claim_amount = input("  Enter the claim amount: ").strip()
                print()
                if claim_amount == "":
                    print()
                    print(
                        f"{RED}Data Entry Error - Claim amount cannot be empty. Please try again.{RESET}")
                    continue
                # Reassigning claim_amount with its float value
                claim_amount = float(claim_amount)
                if claim_amount <= 0:
                    print()
                    print(
                        f"{RED}Data Entry Error - Claim amount cannot be 0. Please try again.{RESET}")
                    continue
                break
            except ValueError:
                print()
                print(
                    f"{RED}Data Entry Error - Invalid input. Please enter a valid numerical value.{RESET}")

        # Format the claim amount as a dollar amount to store in our dictionary.
        formatted_claim_amount = FV.FDollar2(claim_amount)

        claims.append({
            "claim_number": claim_number,
            "claim_date": claim_date,
            "claim_amount": formatted_claim_amount,
        })

    # Blinking message to simulate processing, followed by clearing the terminal to increase readability.
    receipt_blinker()
    clear_terminal()
    # Return the collected claims
    return claims


def format_dollar_values(*args):
    """
    Formats multiple values as dollar amounts (2 decimal places, $ in front).

    Args:
    *args: Any number of values can be formatted.

    Returns:
    A list of formatted values.
    """
    formatted_values = []
    for value in args:
        formatted_values.append(FV.FDollar2(value))
    return formatted_values


def repeat_program():
    """
    Function to ask the user if they want to enter another customer. Accepts "Y" or "N" input.
    If Y, clears the terminal and continues the program.
    If N, clears the terminal and exits the program.
    If invalid input, prompts the user to enter "Y" or "N" again.
    """
    print()
    while True:
        print()
        repeat = input(
            f"{RED}  Do you want to enter another customer? (Y/N): {RESET}").upper()
        print()
        if repeat == "Y":
            clear_terminal()
            break
        elif repeat == "N":
            clear_terminal()
            print()
            print(
                f"{GREEN}Thank you for using One Stop Insurance Group!{RESET}")
            exit()
        print()
        print(f"{RED}Invalid input. Please enter 'Y' or 'N'.{RESET}")
        print()
