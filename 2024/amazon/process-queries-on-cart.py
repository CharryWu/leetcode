# https://www.fastprep.io/problems/amazon-process-queries-on-cart
from typing import *
from collections import defaultdict, deque

class Solution:
    def processQueriesOnCart(self, items: List[int], query: List[int]) -> List[int]:
        """
        Items to be added are added to the end of cart, doesn't affect items to be removed
        So we can add positive items to cart first, then remove from front of cart
        To keep track of which items are to be removed, we use a mapping from value to their index positions
        Each removal removes a position from front of the mapping[val]
        Finally we construct the result by adding all remaining positions from mapping and sort to maintain their relative order
        """
        to_remove = []
        for q in query:
            if q > 0:
                items.append(q)
            else:
                to_remove.append(-q)

        mapping = defaultdict(deque) # value => occurrence pos [index1, index2, ...]
        for i, item in enumerate(items):
            mapping[item].append(i)

        for val in to_remove:
            mapping[val].popleft()

        res = [] # construct
        for item, idxlist in mapping.items():
            for idx in idxlist:
                res.append(idx)
        res.sort()
        return list(map(lambda idx: items[idx], res))



print(Solution().processQueriesOnCart([1, 2, 1, 2, 1], [-1, -1, 3, 4, -3]))
print(Solution().processQueriesOnCart([5, 1, 2, 2, 4, 6], [1, -2, -1, -1]))
