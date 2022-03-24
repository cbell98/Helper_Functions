# Moving windows


# Write a function that processes an input array, returning an array with the difference between each two subsequent elements.
# For example, if the first two elements in the input are 10 and 6 and 15, then the first two elements in
# the output will be 4 and -9. (Because 10-6=4 and 6-15=-9.)
# Note that the output array will have one fewer elements than the input.
def solution(a):
    result = []
    
    window = 2
    
    for start in range(0, len(a) - window + 1):
        
        for i in range(0 + start, window + start):
            diff = (a[0 + start] - a[window + start - 1])
        
        result.append(diff)
        
    return result


# Write a function that moves a "window" over an array, processing the values under the window as it goes.
# For example, a window of size 3 moving across an array of length 9 might look like this for the first 3 
# moves (window is the bar over the values):
def is_even(x):
    return x % 2 == 0

def solution(a, window_size):
    result = []
    
    for start in range(0, len(a) - window_size +1):
        all_odd = True
        
        for i in range(0 + start, window_size + start):
            if is_even(a[i]):
                all_odd = False
        
        result.append(all_odd)
    
    return result


# Write a function that moves a "window" over an array, processing the values under the window as it goes.
# For example, a window of size 3 moving across an array of length 9 might look like this for the first 3 
# moves (window is the bar over the values):
def solution(a, window_size):
    result = []
        
    for start in range(0, len(a) - window_size +1):
        sum = 0
        
        for i in range(0 + start, window_size + start):
            sum += a[i]
            
        average = sum / window_size
        
        result.append(average)
    
    return result


# You are given an array of integers a. Your task is to calculate how many numbers in the array are equal to 
# the arithmetic mean of their immediate neighbors. In other words, count the number of indices i such that 
# a[i] = (a[i - 1] + a[i + 1]) / 2. Note: If a[i - 1] or a[i + 1] don't exist, they should be considered equal to 0.
def solution(a):
    
    a = [0] + a + [0]
    
    count = 0
    
    for i in range(len(a)-2):
        left = a[i]
        middle = a[i+1]
        right = a[i+2]
        
        avg = (left + right) / 2
        
        if middle == avg:
            count += 1

    return count


# Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would 
# be asked to do during a real interview. Implement a function that takes two strings, s and x, as arguments and 
# finds the first occurrence of the string x in s. The function should return an integer indicating the index 
# in s of the first occurrence of x. If there are no occurrences of x in s, return -1.
def solution(s, x):
    
    window = len(x)
    
    for start in range(0, len(s) - window + 1):
        
        value = ""
        
        for i in range(0 + start, window + start):
            value += s[i]
        
        if value == x:
            return start           
        
    return -1


# Given a string s consisting of small English letters, find and return the first instance of a non-repeating 
# character in it. If there is no such character, return '_'.


# You're given an array of integers a. Let's call (a[i - 1], a[i], a[i + 1]) a good tuple, if exactly 2 out of 
# the 3 numbers in it are equal. For example, (2, 1, 2) is a good tuple, but (1, 1, 1) and (1, 2, 3) are not.
# Your task is to return the number of good tuples in a. Note: The tuples may be overlapping.

# In each window, compare three values
def solution(a):
    
    good_tuples = 0
    
    window = 3
    
    for start in range(0, len(a) - window +1):
        
        for i in range(0 + start, window + start):
            
    
            return good_tuples


# You have a string s. Split s into the minimum possible number of increasing substrings. A substring is 
# considered to be increasing when the next symbol in the substring is also next in the English alphabet. 
# This is case sensitive, i.e. 'b' is next for 'a' but 'C' is not next for 'b'. Return an array of these substrings.
def solution(s):

    results = []
    current_str = ''
    
    for i in range(len(s) - 1):
        current_str += s[i]
        if ord(s[i]) != ord(s[i+1]) - 1:
            results.append(current_str)
            current_str = ''
    
    current_str += s[-1]
    
    results.append(current_str)
    
    return results
