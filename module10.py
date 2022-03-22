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


# 
