# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def check(n, head):
            if not n:
                return False
            if not head.next and n.val == head.val:
                return True
            if n.val != head.val:
                return False
            ### POSTCOND: n.val == head.val
            if check(n.left, head.next):
                return True
            if check(n.right, head.next):
                return True

            return False

        res = False
        def traverse(n):
            nonlocal res
            if not n or res:
                return
            if check(n, head):
                res = True
            traverse(n.left)
            traverse(n.right)
        
        traverse(root)
        return res