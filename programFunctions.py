# Importing required modules.
import os
import datetime
import FormatValues as FV
import string
import time
import sys

current_time = datetime.datetime.now()
current_hour = current_time.hour
time_of_day = FV.time_of_day(current_hour)

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
    print()
    for _ in range(2):  # Change to control number of 'blinks'
        print(f"{GREEN}    Processing Policy Information...{RESET}", end="\r")
        time.sleep(0.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)


def saving_blinker():
    for _ in range(5):  # Change to control number of 'blinks'
        print("          Saving claim data...", end="\r")
        time.sleep(0.3)  # To create the blinking effect
        # Clears the entire line and carriage returns
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)
    print()
    print(GREEN + "      Policy data - successfully saved", end="\r" + RESET)
    print()


def receipt_blinker():
    print()
    print()
    for _ in range(4):
        print(f"{GREEN}        PROCESSING YOUR RECEIPT{RESET}", end="\r")
        time.sleep(0.3)
        # Flush the output buffer to make sure the message is displayed immediately
        sys.stdout.flush()
        time.sleep(0.3)
        # Clears the entire line and carriage returns
        sys.stdout.write("\033[2K\r")
        time.sleep(0.3)


def get_customer_full_name():
    """
    Function calls for user input of first and last name.

    Returns the customer's full name.
    """
    # First name input - strip the strong and check for only alphabetic characters.
    while True:
        first_name = input("Enter the customer's first name: ").strip()
        if first_name.isalpha():
            break
        print(
            f"{RED}Data Entry Error - First name must contain only alphabetic characters. Please try again.{RESET}"
        )

    # Last name input - strip the strong and check for only alphabetic characters.
    while True:
        print()
        last_name = input("Enter the customer's last name:  ").strip()
        if last_name.isalpha():
            break
        print(
            f"{RED}Data Entry Error - Last name must contain only alphabetic characters. Please try again.{RESET}"
        )

    # Concatenating and formatting the customer's full name for return.
    return first_name.title() + " " + last_name.title()


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
    else:
        return "night"


def print_greeting(current_hour, full_name):
    """
    Accepts the time of day and the customer's full name.
    """

    time = time_of_day(current_hour)
    print()
    print()
    print(f"               Good {time}, {full_name}!")
    print("   We are excited to offer you a new insurance policy today.")
    print("         Let's move on to your address information.")
    print("==============================================================")
    print()
    print()


def get_customer_info():
    """
    Function calls for user input of address, city, province, postal code, and phone number.

    Returns the customer's address, city, province, postal code, and phone number.
    """
    # User address input.
    while True:
        address = input("Enter the customer's address: ").title()
        if all(char in ALLOWED_CHARACTERS for char in address):
            break
        print()
        print(f"{RED}Data Entry Error - Invalid address. Please try again.{RESET}")

    # User city input.
    while True:
        print()
        city = string.capwords(input("Enter the customer's city: "))
        if not all(char in ALLOWED_CHARACTERS for char in city):
            print()
            print(
                f"{RED}Data Entry Error - Invalid character used. Please try again.{RESET}"
            )
        else:
            break

    # Province input.
    while True:
        print()
        province = input(
            "Enter the customer's province (2 letter abbreviation): ")
        validated_province = FV.validate_province(province)
        if validated_province:
            province = validated_province
            break
        print()
        print(
            f"{RED}Data Entry Error - Please enter a valid province abbreviation.{RESET}"
        )

    # Postal code input - Explained in FormatValues.py
    while True:
        print()
        postal_code = input("Enter the customer's postal code (X#X#X#): ")
        check_post_code = FV.check_postal_code(postal_code)
        if check_post_code.startswith("Data Entry Error"):
            print()
            print(f"{RED}{check_post_code}{RESET}")
            continue
        postal_code = check_post_code
        break

    # Phone number input - Explained in FormatValues.py.
    while True:
        print()
        phone_number = input(
            "Enter the customer's phone number (##########): ")
        # Check if the phone number is valid length, and all digits, return an error message if it's not & return the formatted phone number if it is.
        check_phone_num = FV.check_phone_num(phone_number)
        if len(check_phone_num) != 14:
            print()
            print(f"{RED}{check_phone_num}{RESET}")
            continue
        elif len(check_phone_num) == 14:
            print()
            print(
                f"{GREEN}Phone number successfully validated. {RESET}")
            print()
            phone_number = check_phone_num
        break

    return address, city, province, postal_code, phone_number


def get_insurance_info(full_name, discount_rate):
    """
    Function calls for user input of the number of cars to be insured, 

    Returns the number of cars to be insured, extra liability coverage, glass coverage, and loaner car coverage.
    """
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
                print(
                    f"{RED}Data Entry Error - Number of cars insured cannot be less than 1. Please try again.{RESET}"
                )
                continue
            elif num_cars_insured > 1:
                print(
                    f"{GREEN}You have entered {num_cars_insured} cars to be insured. This qualifies you for a {discount_rate} discount!{RESET}"
                )
                print()
                break
            elif num_cars_insured == 1:
                print(
                    f"{RED}You have entered {num_cars_insured} vehicle to be insured."
                )
                add_another_vehicle = input(
                    f"Would you like to add another vehicle to qualify for a {discount_rate} discount? (Y/N): "
                ).upper()
                print()
                if add_another_vehicle == "Y":
                    print()
                    print(
                        f"{GREEN}You have chosen to add another vehicle. This qualifies you for a {discount_rate} discount!{RESET}"
                    )
                    print()
                    num_cars_insured += 1
                    break
                elif add_another_vehicle == "N":
                    print(
                        f"{GREEN}You have chosen to insure only {num_cars_insured} car.\nIf you wish to review your policy in the future,\nFeel free to contact us at One Stop Insurance Group.{RESET}"
                    )
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
                f"{RED}Data Entry Error - Number of cars insured must be a valid integer. Please try again.{RESET}"
            )

    # Extra liability coverage input
    while True:
        extra_liability = input(
            "Would you like to add extra liability coverage? (Y/N): "
        ).upper()
        if extra_liability != "Y" and extra_liability != "N":
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}"
            )
            continue
        elif extra_liability == "Y":
            # Display 'Yes' if the user enters 'Y'.
            extra_liability_display = "Yes"
            # Adding a coloured confirmation message to the user.
            print(
                f"{GREEN}Added liability coverage up to $1,000,000 to your policy.{RESET}"
            )
            print()
        elif extra_liability == "N":
            # Display 'No' if the user enters 'N'.
            extra_liability_display = "No"
            # Adding a coloured confirmation message to the user.
            print(f"{RED}No extra liability coverage added to your policy.{RESET}")
            print()
        break

    # Glass coverage input
    while True:
        glass_coverage = input(
            "Would you like to add glass coverage? (Y/N):           "
        ).upper()
        if glass_coverage != "Y" and glass_coverage != "N":
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}"
            )
            continue
        elif glass_coverage == "Y":
            # Display 'Yes' if the user enters 'Y'.
            glass_coverage_display = "Yes"
            # Adding a confirmation message to the user.
            print(
                f"{GREEN}Added Glass coverage to your policy.{RESET}"
            )
            print()
        elif glass_coverage == "N":
            # Display 'No' if the user enters 'N'.
            glass_coverage_display = "No"
            # Adding a confirmation message to the user.
            print(f"{RED}No glass coverage added to your policy.{RESET}")
            print()
        break

    # Loaner car coverage input
    while True:
        loaner_car = input(
            "Would you like to add loaner car coverage? (Y/N):      "
        ).upper()
        if loaner_car != "Y" and loaner_car != "N":
            print()
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}"
            )
            continue
        elif loaner_car == "Y":
            # Display 'Yes' if the user enters 'Y'.
            loaner_car_display = "Yes"
            # Adding a confirmation message to the user.
            print(f"{GREEN}Added Loaner car coverage to your policy.{RESET}")
            print()
        elif loaner_car == "N":
            # Display 'No' if the user enters 'N'.
            loaner_car_display = "No"
            # Adding a confirmation message to the user.
            print(f"{RED}No loaner car coverage added to your policy.{RESET}")
            print()
        break

    return num_cars_insured, extra_liability_display, glass_coverage_display, loaner_car_display


def get_payment_method(total_cost):
    """
    Accepts the total cost of the policy to validate against the potential downpayment amount.

    Returns the payment method and if necessary the down payment amount.
    """
    VALID_PAYMENT_METHODS = ["FULL", "MONTHLY", "DOWN PAY"]
    down_payment_amt = 0

    while True:
        payment_method = input(
            "Enter the payment method (Full, Monthly, or Down Pay): ").upper()

        if payment_method not in VALID_PAYMENT_METHODS:
            print(
                f"{RED}Data Entry Error - Invalid payment method. Please enter a valid payment method.{RESET}")
        elif payment_method == "DOWN PAY":
            while True:
                try:
                    down_payment_amt = float(
                        input("Enter the amount of the down payment: $"))
                    if down_payment_amt <= 0:
                        print(
                            f"{RED}Data Entry Error - Down payment cannot be less than or equal to 0. Please try again.{RESET}")
                        break
                    elif down_payment_amt > total_cost:
                        print(
                            f"{RED}Data Entry Error - Down payment cannot be greater than the total cost. Please try again.{RESET}")
                        break
                    print(
                        f"{GREEN}You have chosen our Down Payment option. {RESET}")
                    down_payment_amt += down_payment_amt
                    return payment_method.title(), down_payment_amt
                except ValueError:
                    print(
                        f"{RED}Data Entry Error - Invalid input. Please enter a numerical value.{RESET}")
        elif payment_method.upper() == "FULL" or payment_method.upper() == "MONTHLY":
            print(
                f"{GREEN}You have chosen our {payment_method.title()} payment option. {RESET}")
            return payment_method.title(), down_payment_amt


def get_claims():
    """
    Function to get claim information from the user. Loops over 3 inputs: claim number, claim date, and claim amount. The user can choose to enter no claims, or multiple claims. 

    Returns a list of dictionaries, where each dictionary represents a claim.
    """
    claims = []

    clear_terminal()
    print()
    print()
    print("                  Last Section - We promise!                 ")
    print("           Let's finish up with claim information.           ")
    print("=============================================================")
    while True:

        while True:
            print()
            claim_number = input(
                "Enter the claim number (#####) (type 'DONE' to finish): ")
            if claim_number.upper() == "DONE":
                return claims  # Exiting the entire function when done.
            if len(claim_number) == 5 and claim_number.isdigit():
                break  # Valid claim number, proceed to date input.
            elif len(claim_number) != 5:
                print(
                    f"{RED}Data Entry Error - Invalid claim number. Please enter 5 total numbers.{RESET}")
            elif not claim_number.isdigit():
                print(
                    f"{RED}Data Entry Error - Invalid claim number. Please enter numerical value.{RESET}")

        while True:
            claim_date = input("Enter the claim date (YYYY-MM-DD): ")
            validated_date = FV.check_date(claim_date)
            if not validated_date.startswith("Data Entry Error"):
                break
            print(f"{RED}{validated_date}{RESET}")

        while True:
            try:
                claim_amount = float(input("Enter the claim amount: "))
                if claim_amount <= 0:
                    print(
                        f"{RED}Data Entry Error - Claim amount must be greater than 0. Please try again.{RESET}")
                    continue
                break
            except ValueError:
                print(
                    f"{RED}Data Entry Error - Invalid input. Please enter a valid numerical value.{RESET}")

        formatted_claim_amount = FV.FDollar2(claim_amount)

        claims.append({
            "claim_number": claim_number,
            "claim_date": claim_date,
            "claim_amount": formatted_claim_amount,
        })

        print()
        repeat = input("Do you want to enter another claim? (Y/N): ")
        if repeat.upper() == "N":
            break  # Exit the loop after no more claims are to be entered.
        elif repeat.upper() != "Y":
            print(
                f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}")

    return claims


def format_dollar_values(*args):
    """
    Formats multiple values as dollar amounts.

    Args:
    *args: Any number of values to be formatted.

    Returns:
    A list of formatted values.
    """
    formatted_values = []
    for value in args:
        formatted_values.append(FV.FDollar2(value))
    return formatted_values
