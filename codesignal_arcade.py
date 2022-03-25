# Given a divisor and a bound, find the largest integer N such that:
# N is divisible by divisor.
# N is less than or equal to bound.
# N is greater than 0.
# It is guaranteed that such a number exists.
def solution(divisor, bound):
    
    for i in range(bound, -1, -1):
        if i % divisor == 0:
            return i

# Given the total number of rows and columns in the theater (nRows and nCols, respectively), and the row and column 
# you're sitting in, return the number of people who sit strictly behind you and in your column or to the left, 
# assuming all seats are occupied.
def solution(nCols, nRows, col, row):
    # need rows behind me exclusive * columns to my left (inclusive)
    columns = nCols - (col - 1)
    rows = nRows - row
    return columns * rows


# n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly 
# the same amount of candy as any other child. Determine how many pieces of candy will be eaten by all the children together. 
# Individual pieces of candy cannot be split.
def solution(n, m):
    pieces = m // n
    return n * pieces


# Given an integer n, return the largest number that contains exactly n digits.
def solution(n):
    string = ""
    
    for i in range(n):
        string += '9'
    
    result = int(string)
    
    return result


# You are given a two-digit integer n. Return the sum of its digits.
