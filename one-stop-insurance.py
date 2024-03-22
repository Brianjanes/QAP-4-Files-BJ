# DESCRIPTION: A program for the One Stop Insurance Company to enter and calculate insurance policy information to its new customers.
# AUTHOR: Brian Janes
# DATE: March 17th, 2024

# Import the required libraries
import datetime
import FormatValues as FV
import sys
import time
import string
import programFunctions as PF

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"

# Define program constants
# Defining valid provinces.


POLICY_NUM = 1944
BASIC_PREM_COST = 869.00
XTRA_CAR_DISCOUNT_RATE = 0.25
XTRA_LIABILITY_COST = 130.00
GLASS_COVERAGE_COST = 86.00
LOANER_COST = 58.00
HST_RATE = 0.15
MONTHLY_PRCSSING_FEE = 39.99

current_time = datetime.datetime.now()
current_hour = current_time.hour
time_of_day = FV.time_of_day(current_hour)

# Define the allowed characters for the address, and city inputs.
ALLOWED_CHARACTERS = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,'-1234567890"
)

# Main Program
# This clears up the terminal.
PF.clear_terminal()
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
    full_name = PF.get_customer_full_name()

    PF.processing_blinker()

    # Cleaning up the terminal for the user to move to address inputs.
    PF.clear_terminal()

    # Greeting the user with their previously entered name based on the time of day.
    PF.print_greeting(time_of_day, full_name)

    # Customer info inuputs.
    customer_info = PF.get_customer_info()

    PF.processing_blinker()

    # Clearing the terminal before a new section of inputs.
    PF.clear_terminal()

    # Formatting this for the next function, for upselling!
    formatted_extra_car_discount_rate = "{:.0f}%".format(
        XTRA_CAR_DISCOUNT_RATE * 100)

    # Policy information inputs.
    insurance_info = PF.get_insurance_info(
        full_name, formatted_extra_car_discount_rate)

    PF.processing_blinker()

    # Destructure the information from the return of the function.
    address, city, province, postal_code, phone_number = customer_info

    # Destructure the information from the return of the function.
    num_cars_insured, extra_liability, glass_coverage, loaner_car = insurance_info

    # Processing for policy information.
    # Calculate insurance premium for the first automobile.
    insurance_premium = BASIC_PREM_COST

    # Calculate discount for additional automobiles.
    if num_cars_insured > 1:
        insurance_premium += (num_cars_insured - 1) * (
            BASIC_PREM_COST * XTRA_CAR_DISCOUNT_RATE
        )

    # Calculate extra costs for additional options.
    extra_costs = 0
    if extra_liability == "Y":
        extra_costs += num_cars_insured * XTRA_LIABILITY_COST
    if glass_coverage == "Y":
        extra_costs += num_cars_insured * GLASS_COVERAGE_COST
    if loaner_car == "Y":
        extra_costs += num_cars_insured * LOANER_COST

    # Calculate total insurance premium.
    total_insurance_premium = insurance_premium + extra_costs

    # Calculate HST.
    hst_cost = total_insurance_premium * HST_RATE

    # Calculate total cost.
    total_cost = total_insurance_premium + hst_cost

    # Destructure the payment method tuple
    payment_type, down_payment = PF.get_payment_method(total_cost)

    # Processing for payment type, invoice date, and premium cost (pre-tax)
    # Calculate monthly payment.
    if payment_type.upper() == "FULL":
        monthly_payment = total_cost / 8
    elif payment_type.upper() == "MONTHLY":
        monthly_payment = (total_cost + MONTHLY_PRCSSING_FEE) / 8
    elif payment_type.upper() == "DOWN PAY":
        monthly_payment = (total_cost - down_payment +
                           MONTHLY_PRCSSING_FEE) / 8

    # Calculate total insurance premium (pre-tax)
    total_insurance_premium_pretax = insurance_premium + extra_costs

    PF.processing_blinker()

    # Claims information inputs.
    claims = PF.get_claims()

    # Calculate invoice date and first payment date.
    invoice_date = datetime.datetime.now().strftime("%Y-%m-%d")
    first_payment_date = (
        (datetime.datetime.now() + datetime.timedelta(days=30))
        .replace(day=1)
        .strftime("%Y-%m-%d")
    )

    # Formatting the dollar values em masse.
    formatted_values = PF.format_dollar_values(down_payment, insurance_premium, hst_cost,
                                               total_cost, monthly_payment, extra_costs, total_insurance_premium_pretax)

    # Desctucture the formatted values.
    down_payment, insurance_premium, hst_cost, total_cost, monthly_payment, extra_costs, total_insurance_premium_pretax = formatted_values

    PF.receipt_blinker()

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
    print(f"    Extra Liability Coverage:         {extra_liability:<3s}")
    print(f"    Glass Coverage:                   {glass_coverage:<3s}")
    print(f"    Loaner Car Coverage:              {loaner_car:<3s}")
    print()
    print(f"    Payment Method:              {payment_type:>8s}")
    # Display Down Payment if payment method is 'Down Pay'.
    if payment_type.upper() == "DOWN PAY":
        print(f"    Down Payment:              {down_payment:>10s}")
    print()
    print(f"    Insurance Premium:         {insurance_premium:>10s}")
    print(f"    Extra Costs Total:         {extra_costs:>10s}")
    print(f"    HST:                       {hst_cost:>10s}")
    print(f"    Total Cost:                {total_cost:>10s}")
    print(f"    Monthly Payment:           {monthly_payment:>10s}")
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
        print(
            f"      {claim['claim_number']}     {claim['claim_date']}  {claim['claim_amount']:>10s}"
        )
        print()
    print(f"      --------------------------------")

    # Display total insurance premium (pre-tax) and save policy data message
    print()
    print(f"      Premium Cost(Pre-tax):{total_insurance_premium_pretax:>10s}")
    print()

    PF.saving_blinker()

    # Increment the policy number by 1.
    POLICY_NUM += 1

    # Housekeeping
    # Ask the user if they want to enter another customer
    print()
    while True:
        repeat = input(
            f"{RED}Do you want to enter another customer? (Y/N): {RESET}"
        ).upper()
        print()
        if repeat == "Y":
            PF.clear_terminal()
            break
        elif repeat == "N":
            PF.clear_terminal()
            print()
            print(f"{GREEN}Thank you for using One Stop Insurance Group!{RESET}")
            exit()
        print()
        print(
            f"{RED}Data Entry Error - Invalid input. Please enter 'Y' or 'N'.{RESET}"
        )
