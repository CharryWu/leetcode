from typing import *
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

########## 384. Shuffle an Array ##########
import random
class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums
        self.cur = nums.copy()

    def reset(self) -> List[int]:
        self.cur = self.original.copy()
        return self.cur

    def shuffle(self) -> List[int]:
        """
        Time O(n) | O(1) Extra Space
        """
        n = len(self.cur)
        for i in range(n-1, 0, -1):
            random_idx = random.randint(0, i)
            self.cur[i], self.cur[random_idx] = self.cur[random_idx], self.cur[i]
        return self.cur

########## 295. Find Median from Data Stream ##########
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
        at the left or right side, then check if the remaining string is a palindrome
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

############ 408. Valid Word Abbreviation ############
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == '0':
                return False
            elif abbr[j].isdigit():
                k = j
                while k < n and abbr[k].isdigit():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False

        return True

############# 560. Subarray Sum Equals K ############
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Time O(N) | Space O(N)
        Use prefix sum and frequency to count how many times prefix sum has seen
        If current prefix sum - k has seen before, it means we have seen prefix sum - k before
        and we have exactly seen[prefix-k] subarrays with sum = k
        """
        seen = Counter()
        seen[0] += 1
        prefix = 0
        res = 0
        for i, num in enumerate(nums):
            prefix += num
            if prefix - k in seen:
                res += seen[prefix-k]
            seen[prefix] += 1
        return res

############# 140. Word Break II ############
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}

        def backtrack(s):
            if s not in memo:
                result = []
                for word in words:
                    wordlen = len(word)
                    if s[:wordlen] == word:
                        if len(s) == wordlen:
                            result.append(word)
                        else:
                            for newword in backtrack(s[wordlen:]):
                                result.append(word + " " + newword)
                memo[s] = result
            return memo[s]

        return backtrack(s)

############# 1031. Maximum Sum of Two Non-Overlapping Subarrays ############
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i] + num

        def maxsum(len1, len2):
            """
            |...| arr1 | ... | arr2 | ... |
                len1^       len2^  i^
            In each iteration, we consider two arrays
            arr1 = nums[i-len2-len1:i-len2] and
            arr2 = nums[i-len2:i]

            These two arrays are used to update two sum variables, maxl and ans
            maxl is the maximum sum of ANY subarray size len1 to the left of arr2, in the range of nums[0:i-len2]
            res is the combined sum of ANY TWO non-overlapping subarrays size len1 and len2

            `maxl` is only updated when we encounter a bigger arr1 sum:
                prefix[i-len2]-prefix[i-len1-len2]
            `res` is only updated when we encounter a bigger maxl AND bigger arr2 sum:
                maxl + prefix[i] - prefix[i-len2]

            The finaly result is given by `res`. However, since firstLen and secondLen can differ,
            we run the above algorithm with different parameters
                len1 = firstLen, len2 = secondLen;
                len1 = secondLen, len2 = firstLen
            """
            maxl, ans = 0, 0
            for i in range(len1+len2, len(prefix)):
                maxl = max(maxl, prefix[i-len2]-prefix[i-len1-len2])
                ans = max(ans, maxl + prefix[i] - prefix[i-len2])
            return ans

        return max(maxsum(firstLen, secondLen), maxsum(secondLen, firstLen))

############# 22. Generate Parentheses ############
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(opencount, closecount, path):
            if opencount > n or closecount > n:
                return
            if opencount == closecount == n:
                res.append(''.join(path))
                return

            # two options: place ( or )
            # limitation: cannot place ) if closecount >= opencount
            path.append('(')
            backtrack(opencount+1, closecount, path)
            path.pop()

            if closecount < opencount:
                path.append(')')
                backtrack(opencount, closecount+1, path)
                path.pop()

        backtrack(0, 0, [])
        return res


############# 39. Combination Sum ############
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        N = len(candidates), T = target, M = min(candidates)
        N-ary Tree height = T/M
        Total nodes in N-ary tree = N^(T/M+1)
        Time O(N^(T/M+1)) | Space O(T/M)
        """
        candidates.sort()
        n = len(candidates)
        res = []
        def backtrack(i, path, total):
            if total == target:
                res.append(path.copy())
                return
            elif total > target:
                return

            else:
                for j in range(i, n):
                    # If candidates contains duplicates, need to skip by checking (j > 0 and candidates[j] == candidates[j-1])
                    path.append(candidates[j])
                    backtrack(j, path, total+candidates[j])
                    path.pop()

        backtrack(0, [], 0)
        print(res)
        return res


############# 21. Merge Two Sorted Lists ############
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
            else:
                cur.next = list2
                list2 = list2.next
                cur = cur.next

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next

############# 129. Sum Root to Leaf Numbers ############
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, parentVal):
            nonlocal res
            if not node.left and not node.right:
                res += (parentVal+node.val)
                return

            if node.left:
                dfs(node.left, (parentVal+node.val)*10)
            if node.right:
                dfs(node.right, (parentVal+node.val)*10)
        dfs(root, 0)
        return res

############# 1570. Dot Product of Two Sparse Vectors #############
class SparseVector:
    def __init__(self, nums):
        """
        Each non-zero value is saved as a (index, value) tuple
        """
        self.val = [(idx, num) for idx, num in enumerate(nums) if num != 0]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        Use two pointers i, j, pointing to self and vec
        if self[i] and vec[j] points to same position, can do dot product;
        if point to different position, product is zero, move pointer to smaller index to next
        """
        i, j = 0, 0
        res = 0

        while i < len(self.val) and j < len(vec.val):
            if self.val[i][0] == vec.val[j][0]: # if index is same, can do dot product
                res += self.val[i][1] * vec.val[j][1]
                i += 1
                j += 1
            elif self.val[i][0] < vec.val[j][0]: # index not same, product is zero, skip to next
                i += 1
            else:
                j += 1
        return res

############# 76. Minimum Window Substring ############
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        window, need = Counter(), Counter(t)
        res = ""

        def isValid(window, need):
            for c in need.keys():
                if window[c] < need[c]:
                    return False
            return True

        i = 0
        for j, c in enumerate(s):
            window[c] += 1
            while i <= j and isValid(window, need):
                if j-i+1 < len(res) or res == "":
                    res = s[i:j+1]
                window[s[i]] -= 1
                i += 1
        return res

############# 71. Simplify Path ############
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip('/')
        path = path.split('/')
        res = []
        for p in path:
            if p == '' or p == '.':
                continue
            elif p == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(p)
        return '/' + '/'.join(res)


############# 1209. Remove All Adjacent Duplicates in String II ############
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue

            # either c belongs to last consecutive k duplicate characters
            # or c is a different character
            if stack[-1][0] == c:
                stack[-1] += c
            else:
                stack.append(c)

            # remove stack[-1] if it is too long
            while stack and len(stack[-1]) >= k:
                top = stack.pop()
                top = top[:len(top)-k]
                if top != "": # has residual after remove k characters, add it back
                    stack.append(top)
                # merge last two strings if equal
                if len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                    stack.append(stack.pop() + stack.pop())
        return ''.join(stack)

############# 525. Contiguous Array ############
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        seen = {0: -1}
        res = 0
        parity = 0
        for j, c in enumerate(nums):
            if c == 0:
                parity -= 1
            else:
                parity += 1
            if parity not in seen:
                seen[parity] = j
            else:
                res = max(res, j-seen[parity])
        return res


############# 56. Merge Intervals ############
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort() # do normal sort of based on start value so mergeable intervals are next to each other

        output = [intervals[0]]

        for start, end in intervals:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start, end])
        return output

############# 426. Convert Binary Search Tree to Sorted Doubly Linked List #############
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        思路：输入是bst，所以可以利用中序遍历 guarantee 访问的顺序是从小到大的。
        利用一个 last 指针指向上个中序遍历节点，将其和当前node节点连接
        再利用一个 first 指针指向第一个（最小）节点，在所有遍历完成之后将其和 last 指针互相连接完成闭环
        """
        if not root:
            return None

        first, last = None, None
        def dfs(node):
            """
            1. 递归调用 node.left
            2. 将当前节点 node 和上一个中序遍历节点 last 连接起来 或赋值 first 指针。
               每次中序遍历总是更新 last 指针指向当前node
            3. 递归调用 node.right

            返回值：不需要返回任何值，所有修改节点指针操作均为 in-place
            """
            nonlocal first
            nonlocal last
            if not node:
                return
            dfs(node.left)
            if last:
                last.right = node
                node.left = last
            else:
                first = node
            last = node
            dfs(node.right)
            return

        dfs(root)
        first.left = last
        last.right = first
        return first


############# 236. Lowest Common Ancestor of a Binary Tree ############
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        情况 1，如果 p 和 q 都在以 root 为根的树中，函数返回的即使 p 和 q 的最近公共祖先节点。

        情况 2，那如果 p 和 q 都不在以 root 为根的树中怎么办呢？函数理所当然地返回 null 呗。

        情况 3，那如果 p 和 q 只有一个存在于 root 为根的树中呢？函数就会返回那个节点。
        """
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 情况 1，如果 p 和 q 都在以 root 为根的树中，那么 left 和 right 一定分别是 p 和 q（从 base case 看出来的）。
        if left and right: # 左右子树存在 p 和 q
            return root
        # 情况 2，左右子树都找不到 p 或 q，直接返回 null 表示当前子树不符合题目条件
        if not left and not right:
            return None
        # 情况 3，如果 p 和 q 只有一个存在于 root 为根的树中，函数返回该节点。
        # Edge case: 如果 p 是 q 的父节点，或 q 是 p 父节点，那么最后返回的也是该父节点
        return left if left else right

############# 1060. Missing Element in Sorted Array ############
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 1
        while i < n:
            diff = nums[i] - nums[i-1]
            if diff > k:
                return nums[i-1] + k
            else:
                k -= (diff-1)
            i += 1

        return nums[n-1] + k

############# 973. K Closest Points to Origin ############
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] # maxheap

        for x, y in points:
            dist = x**2+y**2
            if len(heap) < k or dist < -heap[0][0]:
                heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return list(map(lambda x: (x[1],x[2]), heap))

############# 1047. Remove All Adjacent Duplicates In String #############
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            stack.append(c)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()


        return ''.join(stack)

############ 207. Course Schedule ############
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = defaultdict(list) # prerequisite => descendant

        def dfs(course, mapping, visiting):
            if course in visiting:
                return False # cycle detected
            if len(mapping[course]) == 0: # no descendant
                return True

            visiting.add(course)
            for desc in mapping[course]:
                if not dfs(desc, mapping, visiting): return False
            visiting.remove(course)
            mapping[course] = []

            return True

        for a, b in prerequisites:
            mapping[b].append(a)
        visiting = set()
        for i in range(numCourses):
            if not dfs(i, mapping, visiting):
                return False
        return True

############ 346. Moving Average from Data Stream ############
from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.sum += val
        if len(self.window) > self.size:
            self.sum -= self.window.popleft()

        return self.sum / len(self.window)

############ 227. Basic Calculator II ############
OPERANDS = set('+-*/')
class Solution:
    def calculate(self, s: str) -> int:
        """
        We use a stack to keep track of numbers and intermediate results.
        We iterate through the string, building up numbers digit by digit.
        When we encounter an operator or reach the end of the string, we perform the operation based on the previous sign:

        For '+', we push the number onto the stack.
        For '-', we push the negative of the number.
        For '*', we pop the last number, multiply it by the current number, and push the result.
        For '/', we pop the last number, divide it by the current number (using integer division), and push the result.


        After processing all characters, we sum up all numbers in the stack to get the final result.
        """
        stack = [] # only stores intermediary value result, in the end res == sum(stack)
        num = 0
        lastsign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in OPERANDS or i == len(s)-1:
                # when a new sign is encountered, we flush the current number
                # and immediately compute last expression consisting of stack[-1] OPERAND curnum
                # and reset curnum to zero, and update last sign
                if lastsign == '+':
                    stack.append(num)
                elif lastsign == '-':
                    stack.append(-num)
                elif lastsign == '*':
                    stack.append(stack.pop() * num)
                elif lastsign == '/':
                    stack.append(int(stack.pop() / num)) # caveat: don't use //, because // rounds UP when result is negative

                lastsign = char
                num = 0

        return sum(stack)


############ 16. 3Sum Closest ############
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        diff = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                d = s-target
                if abs(d) < diff:
                    res = s
                    diff = abs(d)
                if d > 0:
                    k -= 1
                elif d < 0:
                    j += 1
                else:
                    return target
        return res

############# 116. Populating Next Right Pointers in Each Node II #############

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(left, right):
            if not left or not right:
                return
            left.next = right
            traverse(left.left, left.right)
            traverse(left.right, right.left)
            traverse(right.left, right.right)
        if root:
            traverse(root.left, root.right)
        return root

############# 117. Populating Next Right Pointers in Each Node II #############
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None
        queue = deque([root])
        while queue:
            sz = len(queue)
            for i in range(sz):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i < sz-1: # don't set the next pointer of last node of the same level,
                    # otherwise it will point to first node of next level
                    node.next = queue[0]
        return root

############# 727. Minimum Window Subsequence ############
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        """
        dp[i][j] stores the LARGEST starting index in s1 of the substring
            where s2 has length i and the window ends at j-1 (s2[:i] is totally included in first j characters s1[:j])

        So dp[i][j] would be:
        if s2[i - 1] == s1[j - 1], this means we could borrow the start index from dp[i - 1][j - 1] to make the current substring valid;
        else, we only need to borrow the start index from dp[i][j - 1] which could either exist or not.

        Finally, go through the last row to find the substring with min length and appears first.
        """
        n, m = len(s1), len(s2)

        # Initialize the DP array, m+1 rows and n+1 columns
        dp = [[-1] * (n + 1) for _ in range(m + 1)] # dp[i][j] stores the LARGEST starting index in s1 of the substring

        # when s2 is empty string, the min window in s1 that includes it is still empty string
        # by definition, dp[i][j] stores largest index of min window that ends at j-1 (or first j chars s[:j])
        # so the min window that includes empty string AND ends at j-1 starts at (s1[j:j] == "")
        for j in range(n + 1):
            dp[0][j] = j # s1[j:j] == "" includes s2[:0] == ""

        # Fill the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # s1[dp[i-1][j-1]:j-1] includes a valid subsequence of s2[:i-1] && s1[j] == s2[i]
                # => s1[dp[i][j]:j] includes a valid subsequence of s2[:i]
                if s2[i - 1] == s1[j - 1]: # current matching s1[j] == s2[i] belongs to same window as s1[j-1] == s2[i-1]
                    dp[i][j] = dp[i - 1][j - 1]
                else: # if no match, need stricter condition: find s2[:i] in first j-1 characters of s1. The start index is same if found
                    dp[i][j] = dp[i][j - 1]


        # Now find the minimum length window
        start, length = 0, n + 1
        for j in range(1, n + 1):
            if dp[m][j] != -1:
                if j - dp[m][j] < length:
                    start = dp[m][j]
                    length = j - dp[m][j]

        return "" if length == n + 1 else s1[start : start + length]

############# 543. Diameter of Binary Tree ############
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            """
            DFS returns the depth of the tree from current root
            Each recursive call updates res with two-way path passing root node
            Leaf node: 0, None node: -1, so adding one to none equals zero (don't contribute to path length)
            """
            nonlocal res
            if not node:
                return -1

            left, right = dfs(node.left), dfs(node.right)
            res = max(res, 2+left+right) # maxlen duo-way path passing current node

            return 1 + max(left, right) # maxlen single-way path from deepest leave up to current node

        dfs(root)
        return res

############# 658. Find K Closest Elements ############
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left+right) // 2
            if x <= arr[mid]:
                right = mid
            else:
                left = mid+1
        center = left
        if center == n or (arr[center] != x and center > 0 and abs(x-arr[center-1]) < abs(x-arr[center])):
            center -= 1
        left, right = center, center # [left, right), right exclusive
        for i in range(k):
            # print(left, right)
            # either decrement left or increment right
            if left == 0:
                right += 1
            elif right >= n:
                left -= 1
            elif x-arr[left-1] < arr[right]-x:
                left -= 1
            elif x-arr[left-1] > arr[right]-x:
                right += 1
            else:
                left -= 1
        return arr[left:right]

############# 88. Merge Sorted Array ############
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = len(nums1)-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

############ 398. Random Pick Index ############
from collections import defaultdict
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, num in enumerate(nums):
            self.d[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.d[target])

############ 865. Smallest Subtree with all the Deepest Nodes ############
############# 1123. Lowest Common Ancestor of Deepest Leaves ############
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if not node:
                return None, 0
            leftfound, leftlevel = dfs(node.left)
            rightfound, rightlevel = dfs(node.right)

            if leftlevel > rightlevel:
                return leftfound, leftlevel+1
            if leftlevel < rightlevel:
                return rightfound, rightlevel+1

            return node, leftlevel+1

        return dfs(root)[0]


############# 16. 3Sum Closest ############
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        diff = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                d = s-target
                if abs(d) < diff:
                    res = s
                    diff = abs(d)
                if d > 0:
                    k -= 1
                elif d < 0:
                    j += 1
                else:
                    return target
        return res


############# 79. Word Search ############
DIR = {(0, 1), (0, -1), (-1, 0), (1, 0)}
VISITED_SENTINEL = '#' # any character that will not appear in word charset
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def backtrack(x, y, wordi):
            if wordi == len(word):
                return True
            if not (0 <= x < m and 0 <= y < n):
                return False # cannot match if out of bound
            if board[x][y] != word[wordi]:
                return False

            original = board[x][y]
            board[x][y] = VISITED_SENTINEL

            for dx, dy in DIR:
                nx, ny = x+dx, y+dy
                if backtrack(nx, ny, wordi+1):
                    board[x][y] = original
                    return True

            board[x][y] = original
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False


############# 791. Custom Sort String ############
from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = ""
        for char in order:
            res += char * freq[char]
            del freq[char]

        for char, f in freq.items():
            res += char * f
        return res

############# 30. Substring with Concatenation of All Words ############
# Solution with illustration https://leetcode.com/problems/substring-with-concatenation-of-all-words/solutions/1753357/clear-solution-easy-to-understand-with-diagrams-o-n-x-w-approach/
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Let wordlen = len(words[0])
        Time O(len(s) * wordlen)
        Use two hashmaps + two pointers
        - `need` one hashmap to count all frequencies of each word in words
        - `window` one to count current each substring's frequency in current window s[left:left+wordlen*len(words)]
        - `matched_substrs` count how many words in window has been matched

        We consider all such windows starting from 0, 1, 2, 3, ... wordlen-1, each time moving left/right pointer by wordlen.
        This problem effectively is a combination of wordlen sliding window problems.
         i  ---> i+w ---> i+2w ----> i+3w ----> i+4w
         (i+1)  ---> (i+1)+w ---> (i+1)+2w ----> (i+1)+3w ----> (i+1)+4w
         (i+2)  ---> (i+2)+w ---> (i+2)+2w ----> (i+2)+3w ----> (i+2)+4w
         (i+3)  ---> (i+3)+w ---> (i+3)+2w ----> (i+3)+3w ----> (i+3)+4w

        If there's a mismatch at right pointer, we move left pointer to right of right pointer because
        any window that includes the mismatch is invalid window. Also we need to reset counter to zero

        If advancing right pointer causes excess of substring in current window, we shrink the window size by wordlen and
        update substring count in `window` hashmap accordingly
        """
        need = Counter(words) # substr => frequency in `words`
        res = []
        wordlen = len(words[0])

        for k in range(wordlen):
            window = Counter() # window substr => frequency in s[left:right], right == i + wordlen*len(words)
            left = k
            matched_substrs = 0 # sum of all frequencies in `window`. matched_substrs == sum(window.values())
            for right in range(left, len(s), wordlen):
                if right + wordlen > len(s): # out of bounds, cannot form window
                    break
                nextsubstr = s[right:right+wordlen]
                if nextsubstr in need: # matched
                    window[nextsubstr] += 1
                    matched_substrs += 1
                    while window[nextsubstr] > need[nextsubstr]: # matched, but excess, need move left pointer till no excess
                        oldsubstr = s[left:left+wordlen]
                        window[oldsubstr] -= 1
                        matched_substrs -= 1
                        left += wordlen
                    if matched_substrs == len(words): # yay! we found a permutation of words
                        res.append(left)
                        window[s[left:left+wordlen]] -= 1
                        matched_substrs -= 1
                        left += wordlen
                else: # mismatch, reset counter, and move left
                    window.clear()
                    matched_substrs = 0
                    left = right + wordlen

        return res
