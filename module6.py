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
