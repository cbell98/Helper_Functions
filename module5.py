# More array and string functions


# Construct a string of p copies of n capital "A"s and m capital "B"s.
# Except if the copy number is evenly divisible by 3, in which case
# insert a string of p capital "X"s instead. Copy numbers begin with 0
# for the first copy. Do not use any built-in string duplication
# functionality to solve this.
def solution(p, n, m):

    a_str = ""
    b_str = ""
    x_str = ""

    for i in range(n):
        a_str += "A"

    for i in range(m):
        b_str += "B"

    for i in range(p):
        x_str += "X"

    ab_str = a_str + b_str

    results = ""

    for i in range(p):
        if i % 3 == 0:
            results += x_str
        else:
            results += ab_str

    return results


# Return a reversed version of a string. If the string is empty,
# return an empty string.
def solution(s):
    reverse = ""

    if s == "":
        return ""
    else:
        for i in range(len(s)-1, -1, -1):
            reverse += s[i]

    return reverse


# This function accepts a string. It should return an array where
# each element is a single letter in the string, in the same order.
# If the input string is empty, return an empty array.
def solution(s):
    array = []

    if s == "":
        return []
    else:
        for i in range(len(s)):
            array.append(s[i])

    return array


# Return the number of occurrences of v in array a. If the array is
# empty, return 0.
def solution(a, v):
    count = 0

    if a == []:
        return 0
    else:
        for i in a:
            if i == v:
                count += 1

        return count


# Return true if two arrays are equal. The arrays are equal if they are
# the same length and contain the same value at each particular index.
# Two empty arrays are equal.
def solution(a, b):
    if a == [] and b == []:
        return True
    elif len(a) == len(b) and a == b:
        return True
    else:
        return False


# Given an array and a value x, return an array with all the elements of
# the original except those with value x.
def solution(a, x):
    new_arr = []

    for val in a:
        if val != x:
            new_arr.append(val)

    return new_arr


# Given an input array a and a second array, filter_array, produce a new array
# that contains only the elements of a that are not in filter_array. The elements
# in the result array should be in the same order that they appeared in array a.
def solution(a, filter_list):
    new_arr = []

    for val in a:
        if val not in filter_list:
            new_arr.append(val)

    return new_arr


# Produce an array of n strings. Each string will contain m uppercase "A"s.
def solution(n, m):
    array = []

    a_str = ""

    for i in range(m):
        a_str += "A"

    for i in range(n):
        array.append(a_str)

    return array


# For two arrays a and b of the same length, let's say a is a cyclic shift of b,
# if it's possible for a to become equal to b by performing cyclic shift operations
# on a - moving 0 or more elements from the beginning of the array to the end of
# the array without changing the order of the elements. You are given an array of
# integers elements. Your task is to check whether elements is a cyclic shift of the
# sorted array [1, 2, ..., elements.length]. Return the number of elements you need
# to move to make elements equal to the sorted array. If elements is not a cyclic
# shift of the sorted array (it's not possible to make them equal), return -1.
Need answer


# You are given an array of integers digits representing the digits of a positive
# integer. For example, digits = [1, 2, 3] represents the integer 123. It is
# guaranteed that digits does not have any leading zeros. Assuming that digits
# represents the integer n, your task is to return an array that represents the
# integer n + 1.
def solution(digits):

    string = ""

    for i in digits:
        string += str(i)

    integer = int(string)

    integer += 1

    array = []

    new_string = str(integer)

    for i in new_string:
        array.append(int(i))

    return array


# Avoid using built-in big integers to solve this challenge. Implement them
# yourself, since this is what you would be asked to do during a real interview.
# Given two binary strings a and b, add them together and return the resulting string.
Need answer


# You are given an array of positive integers arr. You'd like to know how many
# triangles can be formed with side lengths equal to adjacent elements from arr.
# Construct an array of integers of length arr.length - 2, where the ith element
# is equal to 1 if it's possible to form a triangle with side lengths arr[i],
# arr[i + 1], and arr[i + 2], otherwise 0. Return the resulting array of integers.
# Note: A triangle can be formed with side lengths a, b, and c
# if a + b > c, a + c > b, and b + c > a.
def solution(arr):

    new_array = []

    for i in range(len(arr)-2):
        a = arr[i]
        b = arr[i+1]
        c = arr[i+2]

        if a + b > c and a + c > b and b + c > a:
            new_array.append(1)
        else:
            new_array.append(0)

    return new_array
  
