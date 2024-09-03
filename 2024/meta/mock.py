def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# Your previous Plain Text content is preserved below:

# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the left bar.
Running CPython 3.10

# Enjoy your interview!

# Hi are you still here?

# yEs

# sorry I am late, we can do it right now, or you can reschedule with the recuriter, I

# Got it I want to do it now!
# Are we using zoom?
# yes
# can you join zoom?

Q1: Balance Parentheses
Given a string with alpha-numeric characters and parentheses, return a string with balanced parentheses by removing the fewest characters possible. You cannot add anything to the string.

balance("()") -> "()"
balance("a(b)c)") -> "a(b)c"
balance(")(") -> ""
balance("(((((") -> ""
balance("(()()(") -> "()()"
balance(")(())(") -> "(())"
balance(")())(()()(") -> "()()()"

def balance(s):
    stack = [] # (char, index)

    for i, c in enumerate(s):
        if c == '(':
            stack.append((c, i))
        elif c == ')':
            if stack and stack[-1][0] == '(': # matched
                stack.pop()
            else: # unmatched
                stack.append((c, i))

    index_to_remove = set([i for c, i in stack])
    res = []
    for i, c in enumerate(s):
        if i not in index_to_remove:
            res.append(c)
    return ''.join(res)

balance(")(())(") -> "(())"
s = ")(())("
i = 0, stack = [')']
i = 1, stack = [')', '(']
i = 2, stack = [')', '(', '(']
i = 3, stack = [')', '(']
i = 4, stack = [')']
i = 5, stack = [')', '(']

index_to_remove = [0, 5]

hash(0) => O(1)
hash(5)

O(N)

res = "(())"



# Q2: Merge Two Sorted Interval Arrays
# Consider the concept of a 'sorted, non-overlapping interval list' - which is an array of intervals that don't overlap with each other and are sorted by interval start.
# Given two of these interval lists, return a 3rd interval list that is the union of the input interval lists.

# For example:
# Input:
# {[1,2], [3,9]}
# {[4,6], [8,10], [11,12]}
# Output should be:
# {[1,2], [3,10], [11,12]}
# 0   1   2   3   4   5   6   7   8   9  10  11  12
#     [---]   [-----------------------]
#                 [-------]       [------]   [----]
#     [---]   [--------------------------]   [----]


O(m+n)
O(m+n)

def solution(interval1, interval2):
    res = []
    i, j = 0, 0
    while i < len(interval1) and j < len(interval2):
        start, end = -1, -1
        if interval1[i][0] < interval2[j][0]:
            start, end = interval1[i]
            i += 1
        else:
            start, end = interval2[j]
            j += 1

        # two options, either add (start, end) directly or merge with res[-1]
        if not result or result[-1][1] < start:
            result.append((start, end))
        else:
            result[-1][1] = max(end, result[-1][1])

    return res

Running test case quicker
Second question explanation doesn't quite understand
