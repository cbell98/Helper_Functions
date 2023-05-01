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


Blackjack is a two player card game whose rules are as follows:
The player and then the dealer are each given two cards.
The player can then "hit", or ask for arbitrarily many additional cards, so long as their total does not exceed 21.
The dealer must then hit if their total is 16 or lower, otherwise pass.
Finally, the two compare totals, and the one with the greatest sum not exceeding 21 is the winner.
For this problem, cards values are counted as follows: each card between 2 and 10 counts as their face value, 
face cards count as 10, and aces count as 1.
Given perfect knowledge of the sequence of cards in the deck, implement a blackjack solver that maximizes the player's 
score (that is, wins minus losses).

import random

def simulate_game():
    # Generate a deck of cards
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1] * 4
    random.shuffle(deck)

    # Deal initial hands
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    # Player's turn
    while sum(player_hand) <= 21:
        # Determine whether to hit or pass
        if sum(player_hand) < 17:
            player_hand.append(deck.pop())
        else:
            break

    # Dealer's turn
    while sum(dealer_hand) <= 16:
        dealer_hand.append(deck.pop())

    # Determine winner
    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)
    if player_total > 21:
        return -1
    elif dealer_total > 21 or player_total > dealer_total:
        return 1
    elif player_total == dealer_total:
        return 0
    else:
        return -1

def simulate_games(num_games):
    total_score = 0
    for i in range(num_games):
        result = simulate_game()
        total_score += result
    return total_score

# Example usage
num_games = 10000
score = simulate_games(num_games)
print(f"Score after {num_games} games: {score}")


This problem was asked by Morgan Stanley.
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, 
and continuing to go back and forth. This style was called "boustrophedon".
Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

def boustrophedon_order(root):
    if root is None:
        return []

    queue = [root]
    left_to_right = True
    result = []

    while queue:
        level_nodes = []
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if not left_to_right:
            level_nodes.reverse()

        result.extend([node.val for node in level_nodes])
        left_to_right = not left_to_right

    return result


Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, 
such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a binary tree is built such that 
the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to 
a 0 in the prefix, while descending right corresponds to 1.
Here is an example tree (note that only the leaf nodes have letters):

        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.

Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping 
between characters and their encoded binary strings.

import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [Node(freq, char) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.freq + right.freq, left=None, right=None)
        parent.left, parent.right = left, right
        heapq.heappush(heap, parent)
        
    return heap[0]

def traverse_tree(node, code="", code_dict={}):
    if node.char:
        code_dict[node.char] = code
    else:
        traverse_tree(node.left, code + "0", code_dict)
        traverse_tree(node.right, code + "1", code_dict)
        
    return code_dict

def huffman_encoding(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1
    
    huffman_tree = build_huffman_tree(freq_dict)
    code_dict = traverse_tree(huffman_tree)
    
    encoded_data = "".join(code_dict[char] for char in data)
    return encoded_data, huffman_tree

def huffman_decoding(encoded_data, huffman_tree):
    decoded_data = ""
    node = huffman_tree
    for bit in encoded_data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
            
        if node.char:
            decoded_data += node.char
            node = huffman_tree
            
    return decoded_data
