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


