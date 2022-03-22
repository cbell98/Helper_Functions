# Dictionaries


# Count the number of occurrences of certain letters in a string. We want to know the counts of each of a 
# set of letters in the input string. For instance, we might want to know how many as, xs, and js there are.
# You'll return the list of requested counts as an array. If letters is an empty string, return an empty array.
def solution(s, letters):
    
    letter_count = {}
    
    for c in s:
        if c not in letter_count:
            letter_count[c] = 0
        
        letter_count[c] += 1
    
    result = []
        
    for c in letters:
        if c in letter_count:
            result.append(letter_count[c])
        else:
            result.append(0)
    
    return result


# Count all the words in a string, then produce a new string when the count of each word in parentheses follows each word.
# If the string is empty, return an empty string.


# Given a string of lowercase words separated by single spaces, return a string with all duplicate words removed. 
# However, the first occurrence of a duplicate word should be left in place; only the subsequent duplicates should be removed.
# If the string is empty, return an empty string.

