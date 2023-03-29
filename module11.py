# Given three values, return a new linked list containing those values. You have to wrap the values into ListNode() objects.
# JavaScript:
# const new_node = new ListNode(n);
# Python:
# new_node = ListNode(n)
# You do not need to uncomment the ListNode code in the header. That's just there for your reference.
# Note the the tests will show the linked lists as if they are arrays. This is just the visual representation; 
# under the hood, it's a linked list with those values. Return a reference to the head of the new list.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def solution(a, b, c):
    
    a_node = ListNode(a)
    b_node = ListNode(b)
    c_node = ListNode(c)
    
    a_node.next = b_node
    b_node.next = c_node
    
    return a_node


# Above function generalize
def solution(a, b, c):
    nums = [a, b, c]
    
    head = tail = None
    
    for n in nums:
        new_node = ListNode(n)
        
        if head == None:
            head = tail = new_node
        
        else:
            tail.next = new_node
            tail = new_node
    
    return head


# Given a list, return length of the list--i,e, the number of nodes in the list.
# You do not need to uncomment the ListNode code in the header. That's just there for your reference.
# Note the the tests will show the linked lists as if they are arrays. This is just the visual representation; 
# under the hood, it's a linked list with those values.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def solution(head):
    
    count = 0

    if head == []:
        return 0
    else:
        n = head
        while n is not None:
            count += 1
            n = n.next
    
    return count


# Given a list, return the sum of all the values in the list. If the input list is empty, return 0.
# You do not need to uncomment the ListNode code in the header. That's just there for your reference.
# Note the the tests will show the linked lists as if they are arrays. This is just the visual 
# representation; under the hood, it's a linked list with those values.

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def solution(head):
    
    sum = 0

    if head == []:
        return 0
    else:
        n = head
        while n is not None:
            sum += n.value
            n = n.next
    
    return sum


# Given a list, return the value of the tail node in the list. If the input list is empty, return -9999.
# You do not need to uncomment the ListNode code in the header. That's just there for your reference.
# Note the the tests will show the linked lists as if they are arrays. This is just the visual representation; 
# under the hood, it's a linked list with those values.
Need Answer


# Insert a new value at the head of a linked list. You have to wrap the value n into a ListNode() object.
# JavaScript:
# const new_node = new ListNode(n);
# Python:
# new_node = ListNode(n)
# You do not need to uncomment the ListNode code in the header. That's just there for your reference.
# Return a reference to the new head of the list.
Need answer


# Given a list and a value, append the value to the end of the list. You have to wrap the value into a ListNode() object.
# Return a reference to the head of the list.


# Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer. For example, 
# given [10, 7, 76, 415], you should return 77641510.
def largest_number(nums):
    # Convert numbers to strings
    nums = [str(num) for num in nums]
    
    # Define comparison function
    def compare(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    # Sort the list of strings using the custom comparison function
    nums.sort(key=compare)
    
    # Concatenate the sorted list of strings into a single string
    result = ''.join(nums)
    
    # Return the resulting string as the output
    return result


Snakes and Ladders is a game played on a 10 x 10 board, the goal of which is get from square 1 to square 100. On each turn players will roll a six-sided die and move forward a number of spaces equal to the result. 
If they land on a square that represents a snake or ladder, they will be transported ahead or behind, respectively, to a new square.
Find the smallest number of turns it takes to play snakes and ladders.
For convenience, here are the squares representing snakes and ladders, and their outcomes:
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

You can solve this problem using breadth-first search (BFS), which is a common algorithm for finding the shortest path in a graph. 
In this case, the graph consists of the squares on the board, and the edges represent the possible moves from one square to another.

from collections import deque

def snakes_and_ladders():
    # Initialize the board and the start and end squares
    board = list(range(101))
    snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
    start, end = 1, 100
    
    # Initialize the queue with the starting square
    queue = deque([(start, 0)])
    
    # Initialize a set to keep track of visited squares
    visited = set([start])
    
    # Perform BFS until the end square is reached
    while queue:
        square, turns = queue.popleft()
        if square == end:
            return turns
        for next_square in range(square + 1, min(square + 7, 101)):
            if next_square in snakes:
                next_square = snakes[next_square]
            elif next_square in ladders:
                next_square = ladders[next_square]
            if next_square not in visited:
                visited.add(next_square)
                queue.append((next_square, turns + 1))
    
    # If the end square is not reachable, return -1
    return -1
