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
def solution(n):
    
    n = str(n)
    total = 0
    
    for digit in n:
        digit = int(digit)
        total += digit
    
    return total


# Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two 
# neighboring numbers is equal (note that 0 and n - 1 are neighboring, too). Given n and firstNumber, 
# find the number which is written in the radially opposite position to firstNumber.
def solution(n, firstNumber):
    if firstNumber < (0.5 * n):
        return (n/2 + firstNumber)
    else:
        return (firstNumber - (n/2))


# One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically begins 
# counting the length of your ride, in minutes. Off you go to explore the neighborhood. When you finally decide to head back, 
# you realize there's a chance the bridges on your route home are up, leaving you stranded! Unfortunately, you don't have your 
# watch on you and don't know what time it is. All you know thanks to the bike's timer is that n minutes have passed since 00:00.
# Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer in the format hh:mm would show.
def solution(n):
    hours = str(n // 60)
    minutes = str(n % 60)

    total_1 = 0
    for i in range(len(hours)):
        total_1 += int(hours[i])
    
    total_2 = 0
    for j in range(len(minutes)):
        total_2 += int(minutes[j])
    
    return total_1 + total_2


# Some phone usage rate may be described as follows:
# first minute of a call costs min1 cents,
# each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
# each minute after 10th costs min11 cents.
# You have s cents on your account before the call. What is the duration of the longest call (in minutes rounded down 
# to the nearest integer) you can have?
def solution(min1, min2_10, min11, s):
    minutes = 0
    
    if s < min1:
        return 0
    else:
        minutes += 1
        s = s - min1
    
    for i in range(9):
        if s > min2_10:
            minutes += 1
            s = s - min2_10
        else:
            return minutes
    
    while s >= min11:
        minutes += 1
        s = s - min11
    
    return minutes


# 
