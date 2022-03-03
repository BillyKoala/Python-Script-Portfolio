"""
Billy Knight - February 2022

This module will count all upper
& lower case vowels in a string.
The sentence to check has been
hard-coded for demo purposes.
"""

try:
    # Declare & initialise some variables.
    vowel_count = 0
    vowel_ascii_numbers = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117] #
    string_to_check = "Supercalifragilisticexpialidocious From Mary Poppins"

    # Loop through the string and count all upper- and lower-case vowels.
    for i in range(len(string_to_check)):

        vowel_count += 1 if ord(string_to_check[i]) in vowel_ascii_numbers else 0

    # Print the result.
    print("There are {} vowels in \'{}\' ".format(vowel_count, string_to_check))

except Exception as e:
    print(e)

finally:
    pass 