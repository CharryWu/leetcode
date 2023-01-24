class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        the middle element of the given list would form the root of the binary search tree. All the elements to the left of the middle 
        element would form the left subtree recursively. Similarly, all the elements to the right of the middle element will form the 
        right subtree of the binary search tree. This would ensure the height balance required in the resulting binary search tree.
        """
        def findMid(s, e):
            slow, fast = s, s
            while fast != e and fast.next != e: # 注意这里不是把fast和空指针比较，而是和e节点比较
                fast = fast.next.next
                slow = slow.next
                
            return slow
        
        # 把链表左闭右开区间 [begin, end) 的节点构造成 BST
        def build(s, e):
            if s == e: # 因为是左闭右开区间，所以现在已经成空集了
                return None
            # 获取链表左闭右开区间 [begin, end) 的中心节点
            mid = findMid(s, e)
            newRoot = TreeNode(mid.val)
            newRoot.left = build(s, mid)
            newRoot.right = build(mid.next, e)
            return newRoot
    
        return build(head, None)

"""
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        n = 0
        # find size of linkedlist
        node = head
        while node:
            n += 1
            node = node.next
        
        cur = head
        def build(s, e):
            nonlocal cur
            # Invalid case
            if s > e:
                return None
            mid = (s+e) // 2
            # Once left half is traversed, process the current node
            leftTree = build(s, mid-1)
            root = TreeNode(cur.val)
            # 当构建完左子树时候，cur自然而然会走到链表中部
            cur = cur.next
            rightTree = build(mid+1, e)
            root.left = leftTree
            root.right = rightTree
            return root
        return build(0, n-1)
"""