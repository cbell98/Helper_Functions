# Building Arrays

# Create a 2D array of size row_count x col_count. Fill the array with 0.
def make_row(col_count):
    
    row = []
    
    for j in range(col_count):
        row.append(0)
    
    return row

def solution(row_count, col_count):
    
    result = []
    
    for i in range(row_count):
        row = make_row(col_count)
        result.append(row)
    
    return result

  
# Create a 2D array of size row_count x col_count. Fill the array with 0.
# (Another way)
def solution(row_count, col_count):
    
    result = []
    
    for i in range(row_count):
        
        row = []
        
        for j in range(col_count):
            row.append(0)
            
        result.append(row)
    
    return result


# Create a square 2D array of size size x size. Fill the array with 0.
# Then draw a line of 1s down the main diagonal.
# This is called an identity matrix.
def solution(size):
    result = []
    
    for i in range(size):
        row = []
        
        for j in range(size):
            if j == i:
                row.append(1)
            else:
                row.append(0)
        
        result.append(row)
    
    return result


# There is a bug in one line of the code. Find it, fix it, and submit.
# Given a rectangular matrix of characters, add a border of asterisks(*) to it.
def solution(picture):

    answer = ['']

    for i in range((len(picture[0])+2)):
        answer[0] += '*'

    for i in range(len(picture)):
        answer.append('*')
        for j in range(len(picture[0])):
            answer[i + 1] += picture[i][j]
        answer[i + 1] += '*'

    answer.append(answer[0])

    return answer


# Return a substring (part of a string) between two indexes.
# The substring from index a up to (but not including) index b should be returned.
# If a is less than 0, treat it like 0.
# If b is greater than the length of the string, treat it like the length of the string.
# If b is less than a, return an empty string.
def solution(s, a, b):
    
    if a < 0:
        a = 0
    
    if b > len(s):
        b = len(s)
    
    if b < a:
        return ""

    return s[a:b]


# Given a number, return the number of digits. You may not use strings to solve this challenge.
# You might have to get mathy for this one.
def solution(n):
    count = 0
    
    while n != 0:
        n //= 10
        count += 1

    return count


# Write a function that builds an n x n multiplication table.
# The result will be a 2D array. The 0th row and column of the table begin with 1 and end with n.


# This function should scan an array for certain elements and remove them.
def solution(a, x):
    
    new_arr = []
    
    for element in a:
        if element != x:
            new_arr.append(element)
        
    return new_arr


# You have an array p of points on a Cartesian plane. Find and return the minimum possible Euclidian distance 
# between two points with different indices in p. 
Need answer

# An odometer palindrome is the when the mileage on your odometer is the same when the digits are reversed. 
# For example, 123321. Assume your odometer is 6 digits and does not show 10ths of miles/kilometers.
# The question is, for a given current odometer reading, when is the next odometer palindrome?
# If the odometer is currently at a palindrome, we're still interested in the next one.
# The input is an integer, but the result should be a string padding with leading zeros to 6 places.
Need answer
