from better_profanity import profanity

""" 
Billy Knight 

This module will translate user input 
into morse code and output the result. 
"""

# Define the morse code dictionary.
morse_code_dict = {"A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".", "F": ".._.", "G": "__.",
                   "H": "....", "I": "..", "J": ".___", "K": "_._", "L": "._..", "M": "__", "N": "_.",
                   "O": "___", "P": ".__.", "Q": "__._", "R": "._.", "S": "...", "T": "_", "U": ".._",
                   "V": "..._", "W": ".__", "X": "_.._", "Y": "_.__", "Z": "__..", "1": ".____",
                   "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...",
                   "8": "___..", "9": "____.", "0": "_____", " ": "/", "*": "*"}

morse_code_conversion = ""

def remove_duplicate_spaces(args):
    """
    This function will allow only one space
    between words, and remove any others.
    """
    try:
        reformatted_string = ""

        for i in range(len(args)):

            # If the current char is a letter or number, concatenate the return string
            if args[i] != " ": reformatted_string += args[i]

            # If the current char is a space but the previous char wasn't, concatenate the return string
            if args[i] == " " and args[i - 1] != " ": reformatted_string += args[i]

        return reformatted_string

    except Exception as e:
        print(e)

    finally:
        pass

try:
    # Get the user input for conversion.
    user_input = (input("Please Key In Text For Morse Code Conversion: "))

    # Remove any potential leading/trailing white spaces.
    user_input = user_input.strip()

    # Change the user input to upper case to match the dictionary upper case.
    user_input = user_input.upper()

    # Strip out any spaces between words and leave only one.
    user_input = remove_duplicate_spaces(user_input)

    # Asterisk any profanity in the user input.
    user_input = profanity.censor(user_input)

    # Make sure the user keyed something in.
    if len(user_input) > 0:

        # Loop through the user input string.
        for key in user_input:

            # Get the morse code VALUE of the current character KEY from the morse_code_dict.
            if key in morse_code_dict: morse_code_conversion += morse_code_dict.get(key)

        # Add profanity notice above header if detected
        if "*" in user_input:
            print("\nAll Profanity Has Been Asterisked.")

        # Print out the morse code conversion complete with header.
        print("\nUser Input: {}".format(user_input) + "\n\n" + morse_code_conversion)

except Exception as e:
    print(e)

finally:
    pass