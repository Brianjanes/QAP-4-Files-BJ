# DESCRIPTION: A program for the One Stop Insurance Company to enter and calculate insurance policy information to its new customers.
# AUTHOR: Brian Janes
# DATE: March 17th, 2024

# Import the required libraries
import datetime
import FormatValues as FV
import sys
import time

# Define program constants
# Open the defaults file and read the values into variables
f = open('Default.dat', 'r')
POLICY_NUM = int(f.readline())
BASIC_PREM_COST = float(f.readline())
XTRA_CAR_DISCOUNT_RATE = float(f.readline())
XTRA_LIABILITY_DISCOUNT = float(f.readline())
GLASS_COVERAGE_COST = float(f.readline())
LOANER_COST = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PRCSSING_FEE = float(f.readline())
f.close()

# Main Program