"""
Billy Knight - January 2022

This module will calculate the minimum denominations
required for change given. All UK denominations are used.
Decimal points are removed to streamline the processing.
e.g. £6.50 and 650 are both treated the same.
"""

from tkinter import *
from tkinter import messagebox

# Define some local variables here.
denominations = [5000, 2000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
change_given = []
quantity = 0
denomination = 0
remainder = 0

change = input("Please Enter Your Change Amount: ")
"""
Preserve the original user input for 
the header in the 'change_given' array.
"""
static_change = change

# If a decimal point has been input, remove it. We are only using pence from here.
change = change.replace(".", "") if "." in str(change) else change

if change.isnumeric():

    change = int(change)

    if change < 100:  # We are managing change denominations of less than £1 here.
        try:
            # Append a header to the change_given array.
            change_given.append(f"Minimum denominations for " + static_change + "p change.\n")

            # Only use the pence values in the denominations array (50p - 1p).
            for i in range(5, len(denominations)):

                quantity = int((change / denominations[i])) if (int(change / denominations[i])) > 0 else 0

                if change < 100 and quantity > 0:
                    remainder = change % denominations[i]
                    change -= quantity * denominations[i]
                    change_given.append(f"{str(denominations[i])}p x {str(quantity)}")

            # Output the array data.
            for i in range(len(change_given)):
                print(change_given[i])
        except Exception as e:
            print(e)

        finally:
            pass

    else:  # We are managing change denominations >= £1 here.
        try:
            # Append a header to the change_given array.
            change_given.append(f"Minimum denominations for £{static_change} change\n")

            # Use all UK denominations in the denominations array (£50 - 1p)
            for i in range(len(denominations)):
                quantity = int((change / denominations[i])) if (int(change / denominations[i])) > 0 else 0

                if quantity > 0:

                    remainder = change % denominations[i]
                    change -= quantity * denominations[i]

                    if denominations[i] >= 100:  # Manage the pound notes here.
                        change_given.append(f"£{int(denominations[i] / 100)} x {quantity}")

                    else:  # Manage the pennies here.
                        change_given.append(f"{denominations[i]}p x {quantity}")

            # Output the array data.
            for i in range(len(change_given)):
                print(change_given[i])

        finally:
            pass
else:
    messagebox.showerror("User Error", "Please Use Numbers ONLY.\n\nThank You.")
