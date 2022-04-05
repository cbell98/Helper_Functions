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


# You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your 
# XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.
# Given values experience, threshold and reward, check if you reach the next level after killing the monster.
def solution(experience, threshold, reward):
    return experience + reward >= threshold


# You found two items in a treasure chest! The first item weighs weight1 and is worth value1, and the second item weighs weight2 and is worth value2. 
# What is the total maximum value of the items you can take with you, assuming that your max weight capacity is maxW and you can't come back for 
# the items later? Note that there are only two items and you can't bring more than one item of each type, i.e. you can't take two first items or
# two second items.
def solution(value1, weight1, value2, weight2, maxW):
    if (weight1 + weight2) <= maxW:
        return (value1 + value2)
    elif weight1 <= maxW and value1 >= value2:
        return value1
    elif weight2 <= maxW and value2 > value1:
        return value2
    elif weight1 <= maxW:
        return value1
    else:
        return 0


# You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. 
# What is the value of the third integer?
def solution(a, b, c):
    if a == b:
        return c
    if a == c:
        return b
    if b == c:
        return a


# Given integers a and b, determine whether the following pseudocode results in an infinite loop
# while a is not equal to b do
#   increase a by 1
#   decrease b by 1
# Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
def solution(a, b):
    if a == b:
        return False
    if a < (b - 1) and (b - a - 1) % 2 == 1:
        return False
    else:
        return True


# Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the
# four signs: +, -, * or / to obtain a correct expression.
def solution(a, b, c):
    if a+b==c or a-b==c or a*b==c or a/b==c:
        return True
    else:
        return False

    
# In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is declared 
# the winner unless their opponent had already won 5 games, in which case the set continues until one of the players has won 7 games.
# Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final 
# score of score1 : score2.
def solution(score1, score2):
    if (score1 != 6 and score1 != 7) and (score2 != 6 and score2 != 7):
        return False
    
    elif score1 == 6 and score2 < 5:
        return True
    
    elif score1 == 7 and score2 == 5:
        return True
    
    elif score1 == 7 and score2 == 6:
        return True
    
    elif score2 == 6 and score1 < 5:
        return True
    
    elif score2 == 7 and score1 == 5:
        return True
    
    elif score2 == 7 and score1 == 6:
        return True
    
    else:
        return False

    
# Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". 
# Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to 
# put her belief to the test. Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.
# A person contradicts Mary's belief if one of the following statements is true:
# they are young and beautiful but not loved;
# they are loved but not young or not beautiful.
def solution(young, beautiful, loved):
    
    if young and beautiful and loved:
        return False
    
    if not loved and not young:
        return False
    
    if not loved and not beautiful:
        return False
    
    if loved and not young:
        return True
    
    if loved and not beautiful:
        return True
    
    else:
        return True
    
    
# You just bought a public transit card that allows you to ride the Metro for a certain number of days. Here is how it works: upon first 
# receiving the card, the system allocates you a 31-day pass, which equals the number of days in January. The second time you pay for the 
# card, your pass is extended by 28 days, i.e. the number of days in February (note that leap years are not considered), and so on. 
# The 13th time you extend the pass, you get 31 days again. You just ran out of days on the card, and unfortunately you've forgotten 
# how many times your pass has been extended so far. However, you do remember the number of days you were able to ride the Metro during 
# this most recent month. Figure out the number of days by which your pass will now be extended, and return all the options as an array 
# sorted in increasing order.
def solution(lastNumberOfDays):
    if lastNumberOfDays == 31:
        return [28, 30, 31]
    if lastNumberOfDays == 30:
        return [31]
    if lastNumberOfDays == 28:
        return [31]


# Given an integer n, find the minimal k such that: 
# k = m! (where m! = 1 * 2 * ... * m) for some integer m;
# k >= n.
# In other words, find the smallest factorial which is not less than n.
def solution(n):
    if n <= 1:
        return 1
    else:
        if n <= 120 and n > 24:
            return 120
        if n <= 24 and n > 6:
            return 24
        if n <= 6 and n > 2:
            return 6
        if n == 2:
            return 2
        
        
# Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.


# You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic marble into the well, 
# it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. How much money will you make?
def solution(a, b, n):
    dollars = 0
    
    while n > 0:
        dollars += (a*b)
        a += 1
        b += 1
        n -= 1
    
    return dollars


# To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them 
# up and starts with the following warm-up exercise: when the coach says 'L', he instructs the students to turn to the left. Alternatively, 
# when he says 'R', they should turn to the right. Finally, when the coach says 'A', the students should turn around. Unfortunately some 
# students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear 'L' and left when 
# they hear 'R'. The coach wants to know how many times the students end up facing the same direction. Given the list of commands the coach 
# has given, count the number of such commands after which the students will be facing the same direction. 
def solution(commands):

    count = 0
    tally = 0

    for move in commands:
        if move == "L" or move == "R":
            count += 1
        elif move == "A":
            count += 2
            
        if count % 2 == 0:
            tally += 1
    
    return tally


# A little child is studying arithmetic. They have just learned how to add two integers, written one below another, column by column. 
# But the child always forgets about the important part - carrying. Given two integers, your task is to find the result that the child will get.
# Note: The child had learned from this site, so feel free to check it out too if you are not familiar with column addition.
Need answer


# You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:
# The smallest box is size 1, the next one is size 2,..., all the way up to size k. Boxes that have an odd size contain only yellow apples. 
# Boxes that have an even size contain only red apples. Your task is to calculate the difference between the number of red apples and the 
# number of yellow apples.
def solution(k):
    
    red = 0
    yellow = 0
    
    for i in range(1, k+1):
        
        if i % 2 == 0:
            red += (i**2)
        else:
            yellow += (i**2)
    
    return red - yellow


# Define an integer's roundness as the number of trailing zeroes in it. Given an integer n, check if it's possible to increase n's 
# roundness by swapping some pair of its digits.
def solution(n):
    
    n = str(n)
    
    for i in range(len(n)-1, -1, -1):
        if n[i] != "0":
            break
    
    for j in range(i, -1, -1):
        if n[j] == "0":
            return True
    
    return False


# We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each 
# step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or 
# equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there 
# is only one non-zero digit left.
Solution


# When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, 
# will in turn leave another leftover. You have solutionNumber solution in your possession. What's the total number of solution you can burn, 
# assuming that you create new solution as soon as you have enough leftovers?
def solution(candlesNumber, makeNew):
    
    total = 0
    leftovers = 0
    
    while candlesNumber > 0:
        total += candlesNumber
        leftovers += candlesNumber
        
        candlesNumber = leftovers // makeNew
        leftovers = leftovers % makeNew
    
    return total


# Imagine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower 
# right corner. Now let's paint the grid in two colors according to the following rules: 
# A cell is painted black if it has at least one point in common with the diagonal;
# Otherwise, a cell is painted white. Count the number of cells painted black.
Solution


# Given an integer size, return array of length size filled with 1s.
def solution(size):
    row = []
    
    for i in range(size):
        row.append(1)
    
    return row


# Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
def solution(inputArray, elemToReplace, substitutionElem):
    
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
            
    return inputArray


# Reversing an array can be a tough task, especially for a novice programmer. Mary just started coding, 
# so she would like to start with something basic at first. Instead of reversing the array entirely, she 
# wants to swap just its first and last elements. Given an array arr, swap its first and last elements and 
# return the resulting array.
def solution(arr):
    if arr == []:
        return []
    else:
        holder = arr[0]
        arr[0] = arr[-1]
        arr[-1] = holder
    
    return arr


# Given two arrays of integers a and b, obtain the array formed by the elements of a followed by the elements of b.
def solution(a, b):
    for i in range(len(b)):
        a.append(b[i])
    
    return a


# Remove a part of a given array between given 0-based indexes l and r (inclusive).
def solution(inputArray, l, r):
    new_array = []
    
    for i in range(len(inputArray)):
        if i >= l and i <= r:
            continue
        else:
            new_array.append(inputArray[i])
    
    return new_array


# We define the middle of the array arr as follows:
# if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from 
# the beginning of the array and from its end;
# if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from 
# the beginning and from the end of the array differ by one.
# An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, 
# determine if it is smooth or not.
def solution(arr):
    
    if arr[0] == arr[-1]:
            # if arr == []:
            #     return []
    
            if len(arr) == 1:
                middle = arr[0]
        
            if len(arr) == 2:
                middle = arr[0] + arr[1]
    
            if len(arr) % 2 == 1:
                index = int((len(arr) - 1) / 2)
                middle = arr[index]
    
            else:
                index = int(len(arr) // 2)
                index2 = int((len(arr) // 2) - 1)
                middle = arr[index] + arr[index2]
            
            if arr[0] == middle:
                return True
            else:
                return False
 
    else:
        return False


# We define the middle of the array arr as follows:
# if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from 
# the beginning of the array and from its end; if arr contains an even number of elements, its middle is the sum of the two 
# elements whose index numbers when counting from the beginning and from the end of the array differ by one.
# Given array arr, your task is to find its middle, and, if it consists of two elements, replace those elements with the value 
# of middle. Return the resulting array as the answer.
def solution(arr):
    if arr == []:
        return []

    if len(arr) == 1:
        middle = arr[0]

    if len(arr) == 2:
        middle = arr[0] + arr[1]

    if len(arr) % 2 == 1:
        index = int((len(arr) - 1) / 2)
        middle = arr[index]

    else:
        index = int(len(arr) // 2)
        index2 = int((len(arr) // 2) - 1)
        middle = arr[index] + arr[index2]
    
    if len(arr) % 2 == 1:
        return arr
    else:
        arr.pop(index)
        arr.pop(index2)
        new_index = int(len(arr) / 2)
        arr.insert(new_index, middle)
        
        return arr


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative 
# integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue 
# will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help 
# him figure out the minimum number of additional statues needed.
def solution(statues):
    statues.sort()
    the_range = (statues[-1] - statues[0]) + 1
    return (the_range - len(statues))


# Determine if the given number is a power of some non-negative integer.


# Find the number of ways to express n as sum of some (at least two) consecutive positive integers.
Solution


# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by 
# taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. 
# You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.
def solution(n):
    
    area = 1
    increase = 4
    
    if n == 1:
        return 1
    else:
        for i in range(1, n):
            area += increase
            increase += 4
        
    return area


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having
# an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest
# to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional
# statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
def solution(statues):
    statues.sort()
    return ((statues[-1] - statues[0] + 1) - len(statues))


# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing 
# sequence by removing no more than one element from the array. Note: sequence a0, a1, ..., an is considered 
# to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.


# Consider a sequence of numbers a0, a1, ..., an, in which an element is equal to the sum of squared digits of the previous element. 
# The sequence ends once an element that has already been in the sequence appears again. Given the first element a0, find the 
# length of the sequence.
def solution(a0):
    
    dict = {}
    
    while a0 not in dict:
        dict[a0] = 1

        a0 = str(a0)

        new_a0 = []
        for i in range(len(a0)):
            new = int(a0[i])
            new_a0.append(new)

        total = 0
        
        for j in range(len(new_a0)):
            total += (new_a0[j] ** 2)

        a0 = total

    return (len(dict) + 1)


# You work in a company that prints and publishes books. You are responsible for designing the page numbering mechanism in the printer. 
# You know how many digits a printer can print with the leftover ink. Now you want to write a function to determine what the last page 
# of the book is that you can number given the current page and numberOfDigits left. A page is considered numbered if it has the full 
# number printed on it (e.g. if we are working with page 102 but have ink only for two digits then this page will not be considered numbered).
# It's guaranteed that you can number the current page, and that you can't number the last one in the book.
def solution(current, numberOfDigits):
    
    while numberOfDigits > 0:
        new_current = str(current)
        if numberOfDigits < len(new_current):
            return current - 1
        else:
            numberOfDigits -= len(new_current)
            print(numberOfDigits)
            current += 1
    
    return current - 1


# Let's say that number a feels comfortable with number b if a ≠ b and b lies in the segment [a - s(a), a + s(a)], where s(x) is the 
# sum of x's digits. How many pairs (a, b) are there, such that a < b, both a and b lie on the segment [l, r], and each number feels 
# comfortable with the other (so a feels comfortable with b and b feels comfortable with a)?


# We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.
# It follows that the weaker the number, the greater overall weakness it has. For the given integer n, you need to answer two questions:
# what is the weakness of the weakest numbers in the range [1, n]? how many numbers in the range [1, n] have this weakness?
# Return the answer as an array of two elements, where the first element is the answer to the first question, and the second element 
# is the answer to the second question.
def divisor_num(x):
    divisors = 0
    
    for i in range(x, 0, -1):
        if x % i == 0:
            divisors += 1
            
    return divisors

def solution(n):
    array = []
        
    for i in range(n, 0, -1):
        array.append(divisor_num(i))
    
    array = array[::-1]
    
    weak_array = []
    array = array[::-1]
    print(array)
    
    for j in range(len(array)):
        count = 0
        
        for k in range(j, len(array)):
            if array[k] > array[j]:
                count += 1
        
        weak_array.append(count)
    
    weak_array = sorted(weak_array, reverse=True)
    
    result = []
    
    result.append(weak_array[0])
    result.append(weak_array.count(weak_array[0]))
    
    return result


# 
