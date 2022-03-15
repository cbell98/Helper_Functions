# Palindromes and string functions


# Return true if a string is a palindrome.
# A palindrome is a word that is spelled the same forward and backward.
# An empty string is a palindrome.
def solution(s):

    front = 0

    end = len(s) - 1

    while front < end:

        if s[front] != s[end]:
            return False

        front += 1

        end -= 1

    return True

# Return a number with its digits reversed.
# The return value should be an integer.
def solution(n):
    n = str(n)
    
    new_str = ""
    
    for i in range(len(n)-1, -1, -1):
        new_str += n[i]
        
    return int(new_str)

# This function accepts an array. It should return true if the array elements read 
# the same forward and backward, i.e. if the array is a palindrome. An empty array is a palindrome.
def solution(a):
    
    new_arr = []
    
    for i in range(len(a)-1, -1, -1):
        new_arr.append(a[i])
    
    return new_arr == a

# Given an input array a determine the length of the leading "run" of numbers. The run is how many
# numbers at the front of the array are the same. If the array is empty, return 0.
def solution(a):
    
    count = 1
    
    if a == []:
        return 0
    elif len(a) == 1:
        return 1
    else:
        lead = a[0]
        
        for i in range(1, len(a)):
            if lead == a[i]:
                count += 1
            else:
                return count

# Return a slice of array a starting from index start and ending before index end.
# If end is less than or equal to start, return an empty array.
# Note that start and end could be beyond the length of the array.
# They should be clamped between 0 and the length of the array minus 1.
def solution(a, start, end):
    
    if end <= start:
        return []

    if start < 0:
        start = 0
    
    if start > len(a) - 1:
        start = len(a)
    
    if end > len(a) - 1:
        end = len(a)
    
    if end < 0:
        end = 0
    
    return a[start:end]

# Examine an array and determine the length of the longest run of elements. 
# That is, the most of a particular element seen in a row.
def solution(a):
    
    counter = 0
    
    for i in a:
        curr_freq = a.count(i)
        if curr_freq > counter:
            counter = curr_freq
    
    return counter


# Run-length encoding algorithm (RLE) works by taking the occurrence of each repeating 
# character and outputting that number along with a single character of the repeating sequence.
# You need to implement an algorithm that applies the RLE to a given string.
