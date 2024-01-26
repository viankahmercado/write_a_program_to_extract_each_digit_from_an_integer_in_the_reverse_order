# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 11:
# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

#function containing while loop
def extract_digits_reverse(num):
    reversed_digits = []

    while num > 0:
        digit = num % 10
        reversed_digits.append(digit)
        num = num // 10

    print(" ".join(map(str, reversed_digits)))
    
# check by printing the variable
