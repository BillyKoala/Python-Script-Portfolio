# Billy Knight - February 2022

"""
This module will only accept a 16-digit number string,
and convert the first twelve characters to asterisks.
"""

number_limit = 16
asterisk_string = ""
text_request = "Please Enter Your 16 Digit Card Number: "

try:
    # Get the user's 16 digit card number.
    cc_no = input(text_request)

    if len(cc_no) == number_limit:  # Ensure 16 digits have been input.

        for i in range(12): asterisk_string += "*"  # Generate a 12 character "*" string.

        last_four_digits = cc_no[12:16]  # Get the last 4 digits of the card number.

        print(f"Card Number: {asterisk_string}{last_four_digits}")  # Output the reformatted card number.

    else:
        # Incorrect number of digits input.
        print(f"\nCard Length Error: {text_request}")

except Exception as e:
    print(e)

finally:
    pass
