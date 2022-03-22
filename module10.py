# Compute the value f(n) for a number of input integers, nums, where f() is an expensive, time-consuming function.
# Return the results of f(n) in an array. Hint: cache the results of previous calls to keep them from timing out.
# Add this function f() before your code for solution().
def f(n):
    r = 1
    
    for i in range(5000000):
        r = ((r + n) * n) % 9973
        
    return r


def solution(nums):
    result = []
    
    cache = {}
    
    for n in nums:
        if n not in cache:
            cache[n] = f(n)
        
        result.append(cache[n])
    
    return result


# Produce a histogram of word frequency in a string. The function should return an array of strings, where each string takes the form:
# word: ####
# word is the word in question, followed by a colon and a space, followed by a number of hash marks that corresponds to the number of 
# times that word appears in the input string. The result array should be sorted alphabetically. This can be done by calling .sort() 
# of the array before returning it. If the input string is empty, return an empty array.
def solution(s):

# Separate string s into list of words s (do i need to do this?)
    s = s.split()
        
    cache = {}

    for word in s:
        if word not in cache:
            cache[word] = ""
        
        cache[word] += "#"
    
    result = []
    
    for word in cache:
        result.append(f"{word}: {cache[word]}")
    
    result.sort()
    
    return result


# 
