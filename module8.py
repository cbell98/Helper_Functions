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


# 
