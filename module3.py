# String functions

# Compute the factorial of an integer n.
# This is commonly written as n!, which is read as "n factorial".
# Using For-Loop
def solution(n):

    factorial = 1

    if n == 0:
        return 1
    elif n < 0:
        return "No Factorial Exists"
    else:
        for i in range(1, n+1):
            factorial = factorial * i
        return factorial


# Compute the factorial of an integer n.
# This is commonly written as n!, which is read as "n factorial".
# Using Recursion
def solution(n):
    if n == 1:
        return 1
    else:
        # Recursive call to the function
        return (n * solution(n-1))


# Compute the product of all numbers from a to b, inclusive
def solution(a, b):

    product = 1

    for i in range(a, b+1):
        product = product * i
    return product


# Return the length of a string
def solution(s):
    return len(s)


# Return the character at index n in a string s
def solution(s, n):
    if n >= len(s) or n < 0:
        return "none"
    else:
        return s[n]


# Return an uppercase version of the input string.
def solution(s):
    return s.upper()


# Return true if a string is all lowercase.
def solution(s):
    return s.islower()


# Count the number of occurrences of a letter in a string
def solution(s, letter):
    count = 0

    for i in s:
        if i == letter:
            count = count + 1
    return count


# Given a number, return the number of digits
def solution(n):
    return len(str(n))


# Return the index of the last character in a string.
# If the string is empty, return -1.
def solution(s):
    if s == "":
        return -1
    else:
        return len(s) - 1


# Return the last character in a string.
# If the string is empty, return "none".
def solution(s):
    if s == "":
        return "none"
    else:
        return s[len(s)-1]


# Return true if the first and second characters in the string are equal
def solution(s):
    if s[0] == s[1]:
        return True
    else:
        return False


# Return true if the first and last characters in the string are equal
def solution(s):
    if s[0] == s[len(s)-1]:
        return True
    else:
        return False


# Return true if the last two characters in the string are equal
def solution(s):
    if s[-1] == s[-2]:
        return True
    else:
        return False


# Return a lowercase version of the input string
def solution(s):
    return s.lower()


# Return true if a string is all uppercase
def solution(s):
    return s.isupper()


# For a given string, return a new string with asterisks (*)
# on each side of each letter. If the string is empty, return an empty string.
def solution(s):
    if s == "":
        return ""
    else:
        newstring = ""
        for char in s:
            newstring += f"*{char}*"
        return newstring


# For a given string, return a new string with asterisks (*)
# on each side of each letter. If the string is empty, return a single asterisks.
def solution(s):
    if s == "":
        return "*"
    else:
        newstring = ""
        for char in s:
            newstring += f"*{char}"

        return newstring + "*"


# For a given string, return the letter that's highest in the alphabet
def solution(s):
    max = 'a'

    for i in range(len(s)):
        if s[i] > max:
            max = s[i]
    return max


# Construct a string of n capital "A"s. You must use a loop
# you can experiment with other built-in string duplication methods after
def solution(n):
    if n == 0:
        return ""
    else:
        return "A"*n
