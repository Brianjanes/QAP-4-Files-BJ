def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to $#,###.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

# Brian'a Additions to this file.

# Function will accept a value that has already been validated through the check_post_code function and format it to X#X #X#.
def format_postal_code(postal_code):
    postal_code = postal_code.upper()
    formatted_postal_code = postal_code[0:3] + " " + postal_code[3:6]
    return formatted_postal_code

# Function will accept a value and check if it is a valid postal code, if it is it will return a formatted postal code, if it is not it will return an error message.
def check_postal_code(postal_code):
    if len(postal_code) != 6:
        return "Data Entry Error (Invalid postal code) - Character count issue. Please try again."
    elif postal_code[0].isalpha() == False or postal_code[2].isalpha() == False or postal_code[4].isalpha() == False:
        return "Data Entry Error (Invalid postal code) - Alphabetical character issue. Please try again."
    elif postal_code[1].isdigit() == False or postal_code[3].isdigit() == False or postal_code[5].isdigit() == False:
        return "Data Entry Error (Invalid postal code) - Numerical character issue. Please try again."
    else:
        return format_postal_code(postal_code)

# Function will accept a value that has already been validated through the check_phone_num function and format it to (###) ###-####.
def format_phone_num(phone_num):
    formatted_phone_num = "(" + phone_num[0:3] + ") " + phone_num[3:6] + "-" + phone_num[6:10]
    return formatted_phone_num

    # Function will accept a value and check if it is a valid phone number, if it is it will return a formatted phone number, if it is not it will return an error message.
def check_phone_num(phone_num):
    if len(phone_num) != 10:
        return "Data Entry Error (Invalid phone number) - Character count issue. Please try again."
    elif phone_num.isdigit() == False:
        return "Data Entry Error (Invalid phone number) - Phone number must only be numerical values. Please try again."
    else:
        return format_phone_num(phone_num)