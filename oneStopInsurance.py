# DESCRIPTION: A program for the One Stop Insurance Company to enter and calculate insurance policy information to its new customers.
# AUTHOR: Brian Janes
# DATE: March 17th, 2024

# Import the required libraries
import datetime
import FormatValues as FV
import programFunctions as PF

# ANSII escape codes to colour text in the terminal.
# Define ANSI escape codes for colors
RED = "\033[91m"
RESET = "\033[0m"
GREEN = "\033[32m"

# Define program constants
# Using a Defaults file to store the default values for the program.
f = open("Default.dat", "r")
POLICY_NUM = int(f.readline())
BASIC_PREM_COST = float(f.readline())
XTRA_CAR_DISCOUNT_RATE = float(f.readline())
XTRA_LIABILITY_COST = float(f.readline())
GLASS_COVERAGE_COST = float(f.readline())
LOANER_COST = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PRCSSING_FEE = float(f.readline())
f.close()

CURRENT_DATE = datetime.datetime.now()

# Formatting this for display purposes in an output.
formatted_extra_car_discount_rate = FV.format_perc_no_decimal(
    XTRA_CAR_DISCOUNT_RATE)

# Main Program Loop
while True:
    # User name inputs function.
    full_name = PF.get_customer_full_name()

    # Customer info inuputs function
    customer_info = PF.get_customer_info(full_name)

    # Policy information inputs function - takes in the full name for header personalization & the discount rate for informing the user about potential savings.
    insurance_info = PF.get_insurance_info(
        full_name, formatted_extra_car_discount_rate)

    # Descructuring the information from the return of the functions we have called to use in processing calculations.
    # Destructure the information from the return of the customer_info().
    address, city, province, postal_code, phone_number = customer_info

    # Destructure the information from the return of get_insurance_info().
    num_cars_insured, extra_liability, glass_coverage, loaner_car = insurance_info

    # Processing calculations with the destructured values to get the total cost of the insurance policy.
    # Calculate insurance premium for the first automobile.
    insurance_premium = BASIC_PREM_COST

    # Calculate discount for additional automobiles.
    if num_cars_insured > 1:
        insurance_premium += (num_cars_insured - 1) * (
            BASIC_PREM_COST * XTRA_CAR_DISCOUNT_RATE
        )

    # Calculate extra costs for additional options.
    extra_costs = 0
    if extra_liability == "Yes":
        extra_costs += (num_cars_insured * XTRA_LIABILITY_COST)
    if glass_coverage == "Yes":
        extra_costs += (num_cars_insured * GLASS_COVERAGE_COST)
    if loaner_car == "Yes":
        extra_costs += (num_cars_insured * LOANER_COST)

    # Calculate total insurance premium.
    total_insurance_premium = insurance_premium + extra_costs

    # Calculate HST.
    hst_cost = total_insurance_premium * HST_RATE

    # Calculate total cost.
    total_cost = total_insurance_premium + hst_cost

    # Payment method inputs.
    payment_info = PF.get_payment_method(
        full_name, total_cost, MONTHLY_PRCSSING_FEE)

    # Descructuring the information from the return of the payment method function to use in processing calculations.
    payment_method, down_payment, monthly_payment = payment_info

    # Calculate total insurance premium (pre-tax)
    total_insurance_premium_pretax = insurance_premium + extra_costs

    # Claims information inputs.
    claims = PF.get_claims()

    # Calculate invoice date and first payment date.
    invoice_date = datetime.datetime.now().strftime("%Y-%m-%d")
    first_payment_date = (
        (datetime.datetime.now() + datetime.timedelta(days=30))
        .replace(day=1)
        .strftime("%Y-%m-%d")
    )

    # Formatting the dollar values en masse.
    formatted_values = PF.format_dollar_values(
        down_payment, insurance_premium, hst_cost, total_cost, extra_costs, total_insurance_premium_pretax)

    # Desctucture the formatted values to be displayed on the receipt.
    down_payment, insurance_premium, hst_cost, total_cost, extra_costs, total_insurance_premium_pretax = formatted_values

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
    print(f"    Extra Liability Coverage:         {extra_liability:>3s}")
    print(f"    Glass Coverage:                   {glass_coverage:>3s}")
    print(f"    Loaner Car Coverage:              {loaner_car:>3s}")
    print()
    print(f"    Payment Method:              {payment_method:>8s}")
    # Display Down Payment if payment method is 'Down Pay'.
    if payment_method.upper() == "DOWN PAY":
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
        print()
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

    f = open("Policies.dat", "a")

    # All values written to file must be a string.  If you have a numeric
    # value, use the str() function to convert.
    f.write("{}, ".format(str(POLICY_NUM)))
    # This is the current system date
    f.write("{}, ".format(str(CURRENT_DATE)))
    f.write("{}, ".format(str(invoice_date)))
    f.write("{}, ".format(str(full_name)))
    f.write("{}, ".format(str(address)))
    f.write("{}, ".format(str(city)))
    f.write("{}, ".format(str(province)))
    f.write("{}, ".format(str(postal_code)))
    f.write("{}, ".format(str(phone_number)))
    f.write("{}, ".format(str(num_cars_insured)))
    f.write("{}, ".format(str(extra_liability)))
    f.write("{}, ".format(str(glass_coverage)))
    f.write("{}, ".format(str(loaner_car)))
    f.write("{}, ".format(str(payment_method)))
    if payment_method.upper() == "DOWN PAY":
        f.write("{}, ".format(str(down_payment)))
    f.write("{}, ".format(str(insurance_premium)))
    f.write("{}, ".format(str(extra_costs)))
    f.write("{}, ".format(str(total_insurance_premium_pretax)))
    f.write("{}, ".format(str(hst_cost)))
    f.write("{}, ".format(str(total_cost)))
    f.write("{}, ".format(str(monthly_payment)))
    f.write("{}, ".format(str(first_payment_date)))
    f.write("{}\n".format(claims))

    f.close()

    PF.saving_blinker()

    # Increment the policy number by 1.
    POLICY_NUM += 1

    # Save the updated policy number to the file
    f = open("Default.dat", "w")
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREM_COST)))
    f.write("{}\n".format(str(XTRA_CAR_DISCOUNT_RATE)))
    f.write("{}\n".format(str(XTRA_LIABILITY_COST)))
    f.write("{}\n".format(str(GLASS_COVERAGE_COST)))
    f.write("{}\n".format(str(LOANER_COST)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(MONTHLY_PRCSSING_FEE)))
    f.close()

    # Housekeeping
    # Ask the user if they want to enter another customer
    PF.repeat_program()
