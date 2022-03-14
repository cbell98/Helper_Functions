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

# 
