# Functions manipulating arrays

# Write a function that returns the length of an array
def solution(a):
    return len(a)


# This function accepts an array and an index. It should return
# the value at that index. If the index is out of range, it should
# return -999. (Out of range means less than 0 or greater than the
# maximum index of the array.)
def solution(a, index):
    if index < 0 or index >= len(a):
        return -999

    return a[index]


# Write a function that prepends front and appends back to an array
def solution(a, front, back):
    a.insert(0, front)
    a.append(back)
    return a


# Write a function that deletes a value from an array a at index
def solution(a, index):
    a.pop(index)

    return a


# Given a number, return the number of digits. You may not use strings
# to solve this challenge. You might have to get mathy for this one.
def solution(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count


# This function should start computing the product of
# x * (x+1) * (x+2) * (x+3) * ...
# until the product becomes evenly divisible by 7
# Then it should stop and return the product
# If x is already divisible by 7, just return x
Need answer


# Write a function that chops off the beginning and end of an
# array and puts them in a new array.  An array containing the
# original array and the new array should be returned.
def solution(a):
    b = []
    b.append(a.pop(0))
    b.append(a.pop())

    return a, b


# Write a function that inserts a new value in the middle of an array.
# The middle index is the length of the array divided by 2, rounded down.
def solution(a, x):
    a.insert(len(a)//2, x)

    return a


# This function accepts an array and a value to search for. It should return
# true if the value occurs anywhere in the array
def solution(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return True

    return False


# This function accepts an array. It should return an array with members
# that are equal to those in the original array multiplied by 2. You can
# modify the existing array and return it, or construct a new one. If the
# input array is empty, an empty array should be returned.
def solution(a):
    members = []

    if a == "":
        return ""
    else:
        for i in range(len(a)):
            members.append(a[i] * 2)

    return members


# This function accepts an array. It should return the sum of all elements
# in the array. If the input array is empty, return 0.
def solution(a):
    sum = 0

    if a == "":
        return 0
    else:
        for i in range(len(a)):
            sum += a[i]

    return sum


# Construct a string of n capital "A"s followed by a string of m capital "B"s
def solution(n, m):
    a = "A" * n
    b = "B" * m

    return a+b


# Construct a string made from every other character in the input string.
# The first character of the input string will be the first character in
# the output string. If the input string is empty, return an empty string
def solution(s):
    t = ""

    if s == "":
        return ""
    else:
        for i in range(0, len(s), 2):
            t += s[i]

    return t


# Construct a string made from every other character in the input string,
# excluding vowels. The first character of the input string will be the first
# character in the output string. If the input string is empty, return an empty
# string. For the purpose of this assignment, "y" is NOT considered a vowel,
# only "a", "e", "i", "o", and "u".
def solution(s):
    t = ""

    if s == "":
        return ""
    else:
        for i in range(0, len(s), 2):
            if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and s[i] != "u":
                t += s[i]

    return t


# Construct a string made from every other character in the input string,
# excluding vowels and capital letters
def solution(s):
    t = ""

    if s == "":
        return ""
    else:
        for i in range(0, len(s), 2):
            if s[i] != "a" and s[i] != "e" and s[i] != "i" and s[i] != "o" and s[i] != "u" and s[i].isupper() == False:
                t += s[i]

    return t


# Given a number and a field width, return a string with that number padded with
# leading zeros. The field width is the total number of digits in the result string,
# not the number of zeros. If the width is smaller than the number of digits in the
# n, return a string containing only n.
Need answer


# Construct a string of p copies of n capital "A"s and m capital "B"s
def solution(p, n, m):
    return p*((n*"A") + (m*"B"))
