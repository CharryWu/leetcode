########## 162. Find Peak Element ##########
class Solution:
    """
    O(log n) time complexity
    O(1) space complexity
    """
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2 or nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        left, right = 1, len(nums)-2
        while left <= right:
            mid = (left+right)//2
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
        return -1

########## 1249. Minimum Remove to Make Valid Parentheses ##########
class Solution:
    """
    O(n) time complexity
    O(n) space complexity
    """
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Let's put all this together into a 2-pass algorithm.
        1. Identify all indexes that should be removed. These are unmatched ")" and "(".
        2. Build a new string with removed indexes.

        Algorithm:
        Loop thru characters in s: 1. skip non "()" characters, 2. add any "("'s index to stack,
        3. any ")" is either matched or unmatched.
            If ")" is matched, pop one "(" from stack,
            If ")" is unmatched, we immediately know it should be removed.

        Finally, if we encounter any
        """
        stack = [] # stack of indexes of '(' or ')'
        index_to_remove = set()

        # process s to obtain stack elements
        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            else:
                if len(stack) == 0: # unmatched )
                    index_to_remove.add(i)
                else: # matched )
                    stack.pop()

        index_to_remove |= set(stack)
        return ''.join([c if i not in index_to_remove else '' for i, c in enumerate(s) ])

########## 1004. Max Consecutive Ones III ##########
class Solution:
    """
    O(n) time complexity
    O(1) space complexity
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Find the max length of sliding window that may contain up to k zeros
        """
        res = 0
        zero_count = 0
        i = 0
        for j, num in enumerate(nums):
            # NO NEED TO CHECK num == 1 since it doesn't affect window size
            # if num == 1:
            #     pass # don't use continue here, we still want to update `res`!
            # elif num == 0:
            if num == 0:
                zero_count += 1
                while zero_count > k and i <= j:
                    if nums[i] == 0:
                        zero_count -= 1
                    i += 1

            res = max(res, j-i+1)
        return res

########## 528. Random Pick with Weight ##########
import random
class Solution:
    """
    Use prefix sum array + binary search to achieve log(n) time
    O(n) time complexity to prepare prefix sum, O(log n) time complexity to search

    Time O(n) | Space O(n)
    """
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        rand = random.random()
        cutoff = rand * self.total
        # find first element greater than or equal to cutoff
        low, high = 0, len(self.prefix)
        while low < high:
            mid = (low + high) // 2
            if cutoff > self.prefix[mid]:
                low = mid + 1
            else:
                high = mid
        return low


########## 314. Binary Tree Vertical Order Traversal ##########
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    """
    Use bfs w/ deque to achieve O(n) time complexity

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Group nodes by column, while maintaining row order inside each group
        Use bfs w/ deque that guarantees row order across each visit, and a hashmap to store all column groups
        """
        columns = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            if node:
                columns[column].append(node.val)
                queue.append((node.left, column-1))
                queue.append((node.right, column+1))

        res = []
        for col in sorted(list(columns.keys())):
            res.append(columns[col])
        return res

########## 50. Pow(x, n) ##########
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Achieve log(n) time complexity using binary exponentiation
        """
        # edge case: 0^n == 0, 1^n == 1, x^1 == n
        if x == 0 or x == 1 or n == 1:
            return x
        if n == 0: # x^0 == 1
            return 1

        # if n is negative, we need to use 1/x instead of x, and flip the sign of n
        if n < 0:
            return self.myPow(1/x, -n)

        # use binary exponentiation
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        else:
            res = self.myPow(x, n//2)
            return res ** 2


import heapq
class MedianFinder:
    """
    Use min-heap to store lower half values, and max-heap to store upper half values
    Time O(log(n)) | Space O(n)
    """
    def __init__(self):
        self.minheap = [] # store upper half values
        self.maxheap = [] # store lower half values

    def addNum(self, num: int) -> None:
        if len(self.minheap) > 0 and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -num)
        # rebalance
        if len(self.minheap) - len(self.maxheap) > 1:
            upper_low = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -upper_low)
        elif len(self.maxheap) - len(self.minheap) > 1:
            lower_high = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, lower_high)

    def findMedian(self) -> float:
        m, n = len(self.minheap), len(self.maxheap)
        if m == n:
            return (self.minheap[0] - self.maxheap[0]) / 2
        elif m > n:
            return self.minheap[0]
        else:
            return -self.maxheap[0]

########## 127. Word Ladder ##########
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Since we're getting MINIMUM transformation needed, use BFS
        """
        if beginWord == endWord:
            return 0
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        mapping = defaultdict(list) # intermediary "c*t" => actual words
        for word in wordset:
            for i in range(len(word)):
                intermediate = word[:i] + '*' + word[i+1:]
                mapping[intermediate].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1 # at least one transformation to reach from beginWord to endWord

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                visited.add(word)

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbor in mapping[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            res += 1
        return 0

########## 133. Clone Graph ##########
class Solution:
    """
    Time O(n) | Space O(n)
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Use dfs to clone
        Need a mapping from newly created node to old node to set up neighbors during dfs
        """
        mapping = {} # old node => new node

        def dfs_clone(node):
            """
            clone node and all its neighbors and adding all neighbors to newnode.neighbors
            """
            if not node:
                return None
            if node in mapping: # if new node has been created, don't create again
                return mapping[node]
            newnode = Node(node.val)
            mapping[node] = newnode
            for n in node.neighbors:
                newnode.neighbors.append(dfs_clone(n))
            return newnode

        return dfs_clone(node)


############# 938. Range Sum of BST #############
class Solution:
    """
    Time O(n) | Space O(h)
    """
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return
            if low <= node.val <= high:
                res += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < low:
                dfs(node.right)
            else:
                dfs(node.left)
        dfs(root)
        return res

############ 215. Kth Largest Element in an Array ############
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [] # maintain a min heap of k elements, push to heap when see larger one
        n = len(nums)
        for num in nums:
            if len(minheap) < k or num > minheap[0]:
                heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]

import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        First, we need to choose so-called pivot and partition element of nums into 3 parts:
            elements, smaller than pivot, equal to pivot and bigger than pivot. (sometimes two groups enough:
            less and more or equal)
        Next step is to see how many elements we have in each group:
            if k <= L, where L is size of left, than we can be sure that we need to look into the left part.
            If k > L + M, where M is size of mid group, than we can be sure, that we need to look into the right part.
        Finally, if none of these two condition holds, we need to look in the mid part,
            but because all elements there are equal, we can immedietly return mid[0].
        Complexity: time complexity is O(n) in average, because on each time we reduce searching range approximately 2 times.
        This is not strict proof, for more details you can do some googling. Space complexity is O(n) as well.
        """
        if not nums: return
        pivot = random.choice(nums)
        left, mid, right = [], [], []
        for num in nums:
            if num > pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]

############ 680. Valid Palindrome II ############
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Time O(n) | Space O(1)
        Two converging pointers, when encounter a mismatch, check if we can delete one character
        at the left or right side
        """
        l, r = 0, len(s)-1

        def checkPali(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while l <= r:
            if s[l] != s[r]: # two possibility of deleting one character: left or right
                return checkPali(s, l+1, r) or checkPali(s, l, r-1)

            l += 1
            r -= 1
        return True
