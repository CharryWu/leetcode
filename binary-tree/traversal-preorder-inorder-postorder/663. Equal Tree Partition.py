class Solution(object):
    def checkEqualTree(self, root):
        """
        When the partition is made, each part should have sum equal to
        exactly half the sum of the total tree
        """
        seen = set()

        def traverse(node, is_root):
            if not node:
                return 0
            leftsum = traverse(node.left, False)
            rightsum = traverse(node.right, False)
            cursum = leftsum + rightsum + node.val
            if not is_root: # don't include root sum into result, we can't partition at any levels above root
                seen.add(cursum)
            return cursum

        total = traverse(root, True)
        # NOTE: MUST USE FLOAT DIVISION, TOTAL SUM OF TREE COULD BE ODD
        return total / 2.0 in seen
