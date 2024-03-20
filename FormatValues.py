import datetime

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


def format_postal_code(postal_code):
    """
    Accepts a value that has already been validated through the check_post_code function and format it to X#X #X#.

    Returns a formatted postal code.
    """
    postal_code = postal_code.upper()
    formatted_postal_code = postal_code[0] + postal_code[1] + postal_code[2] + " " + postal_code[3] + postal_code[4] + postal_code[5]
    return formatted_postal_code

def check_postal_code(postal_code):
    """
    Accepts a value and checks if it is a valid postal code in terms of character count, alphabetical characters, and numerical characters. 

    Returns a formatted postal code or an error message.
    """
    if len(postal_code) != 6:
        return "Data Entry Error (Invalid postal code) - Character count issue. Please try again."
    elif not (postal_code[0].isalpha() and postal_code[2].isalpha() and postal_code[4].isalpha()):
        return "Data Entry Error (Invalid postal code) - Alphabetical character issue. Please try again."
    elif not (postal_code[1].isdigit() and postal_code[3].isdigit() and postal_code[5].isdigit()):
        return "Data Entry Error (Invalid postal code) - Numerical character issue. Please try again."
    else:
        return format_postal_code(postal_code)


def format_phone_num(phone_num):
    """
    Accepts a value that has already been validated through the check_phone_num function and format it to (###) ###-####.

    Returns a formatted phone number.
    """
    formatted_phone_num = "(" + phone_num[0:3] + ") " + phone_num[3:6] + "-" + phone_num[6:10]
    return formatted_phone_num

def check_phone_num(phone_num):
    """
    Accepts a value and checks if it is a valid phone number in terms of character count and numerical characters.

    Returns a formatted phone number or an error message.
    """
    if len(phone_num) != 10:
        return "Data Entry Error (Invalid phone number) - Character count issue. Please try again."
    elif phone_num.isdigit() == False:
        return "Data Entry Error (Invalid phone number) - Phone number must only be numerical values. Please try again."
    else:
        return format_phone_num(phone_num)
