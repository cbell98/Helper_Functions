# Functions

# Write a function that converts a floating point number to a string
# with a specific number of digits past the decimal place.
def solution(f, places):
    y = f"{f:.{places}f}"
    return y


# Write a function that returns true if a number is between 2 and 7, exclusive.
def solution(n):
    if n > 2 and n < 7:
        return True
    else:
        return False


# Return the larger of two characters
def solution(a, b):
    if a > b:
        return a
    else:
        return b


# This function will analyze its input and return a string based on it
def solution(n):
    if n == 0:
        return "none"
    elif n == 1:
        return "one"
    elif n == 2:
        return "two"
    else:
        return "some"


# Return the larger of three numbers
def solution(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return a


# Return the largest of six numbers
def solution(a, b, c, d, e, f):

    numbers = [a, b, c, d, e, f]
    max_num = a

    for number in numbers:
        if number > max_num:
            max_num = number

    return max_num


# This function will run a set of tests on three numbers.
# If the test passes, the function will return the string "OK".
# Otherwise it returns "NOK"
def solution(a, b, c):
    if a > b and b <= c and (a*3) > c:
        return "OK"
    elif a > b and b <= c and c <= a:
        return "OK"
    else:
        return "NOK"


# If there isn't enough in the account to make the withdrawal, return -1.
# Otherwise return the remaining balance after the withdrawal.
def solution(amount, balance):
    if amount > balance:
        return -1
    else:
        return balance - amount


#
