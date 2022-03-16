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
Need answer


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

