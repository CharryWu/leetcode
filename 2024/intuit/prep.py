intarr = [
    [3, 1, 4, 2, 5],
    [9, 1, 3],
    [3, 3],
]

def solution(intarr):
    res = 0
    for row in range(len(intarr)):
        minval, maxval = float('inf'), float('-inf')
        for num in intarr[row]:
            minval = min(minval, num)
            maxval = max(maxval, num)
        res += (maxval - minval)
    return res

def solution2(intarr):
    res = 0
    for row in range(len(intarr)):
        for i, inum in enumerate(intarr[row]):
            if inum == 1:
                continue
            for j in range(i+1, len(intarr[row])):
                jnum = intarr[row][j]
                if jnum == 1:
                    continue
                if inum % jnum == 0:
                    res += inum // jnum
                elif jnum % inum == 0:
                    res += jnum // inum
    return res

print(solution(intarr))
print(solution2(intarr))


from collections import deque
import time
queue = deque()
def rate_limit(key, intervalInSec, maxLimit) -> bool:
    queue.append((key, time.time()))

    while queue and queue[0][1] < time.time() - intervalInSec:
        queue.popleft()

    count = 0
    for i in range(len(queue)):
        if queue[i][0] == key:
            count += 1
            if count > maxLimit:
                return False

    return True


def prettifyJson(s):
    """
    Prettify a JSON string.

    Args:
        s (str): The JSON string to prettify.

    Returns:
        str: The prettified JSON string.
    """

    # Indentation level.
    indent = 0

    # Result string.
    r = ""

    # Iterate over the characters in the JSON string.
    for x in s:
        # If we encounter a '{', we increase the indentation level.
        if x in ['{']:
            indent += 2
            r += x + "\n" + indent * "*"
        # If we encounter a '[', we add newline character and add [ and then increase the indentation level.
        elif x in ['[']:
            # r += "\n" + indent * "*"
            indent += 2
            r += x + "\n" + indent * "*"
        # If we encounter a '}' or ']', we decrease the indentation level.
        elif x in ['}', ']']:
            indent -= 2
            r += "\n" + indent * "*" + x
        # If we encounter a ',', we add a newline and indent the next line.
        elif x in [',']:
            r += x + "\n" + indent * "*"
        # Otherwise, we just add the character to the output string.
        else:
            r += x

    return r


# Example
s = '{"username":"Jonas","devices":["iPhone 13 Pro","Samsung Galaxy S30"]}'

# Pretty print the JSON string.
print(prettifyJson(s))


class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

# use hashmap and double linkedlist, hashmap stores key => Node
# double linked list left = Least Recently Used, right = most recently used
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: key => node
        # dummy nodes for left and right,
        # left = Least Recently Used, right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        # insert at the most recently used
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # TODO: update to most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # re-insert the (key, value) if it already exists (so it's most recently used)
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
