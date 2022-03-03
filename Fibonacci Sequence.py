"""
Billy Knight - February 2022

This module will calculate the
Fibonacci Sequence to the nth term.
"""

fib = []

nth = 10
num1 = 0
num2 = 1
count = 0

while count <= nth:

    if count == 0: fib.append(0)
    if count == 1: fib.append(1)
    fib.append(num1 + num2)
    num1 = num2
    num2 = fib[(len(fib) - 1)]
    count += 1

print(fib)