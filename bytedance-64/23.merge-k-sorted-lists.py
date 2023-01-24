import heapq
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        这题数据结构很重要。因为我们需要总是获取当前 所有list cur node 中的
        最小值，所以需要一个 heap，存 (cur_val, i) 方便快速定位。cur_val = lists[i][j] 的值
        因为heap 里面存的是 head 的值，我们还需要维护一个 list_curs 数组存所有指向 list 当前节点的指针
        最后还需要一个 cur 指针和 dummy_head 来构建返回结果

        主要代码在 while loop 里面，每次循环构建 cur.next并更新 cur。
        然后再将 list_curs[i] 指针指向下一个节点，将其加入 heap 里面

        Edge case:
            lists 中包含空链表
        """
        lists = list(filter(lambda head: bool(head), lists)) # 过滤掉所有空链表
        num_lists = len(lists)
        if num_lists == 0:
            return None

        dummy_head = ListNode(0)
        cur = dummy_head

        heap = [(head.val, i) for i, head in enumerate(lists)]
        list_curs = lists.copy()
        heapq.heapify(heap)

        while heap:
            topval, topi = heapq.heappop(heap)
            cur.next = ListNode(topval)
            cur = cur.next
            nodej = list_curs[topi]
            nodej_next = nodej.next
            if nodej_next:
                heapq.heappush(heap, (nodej_next.val, topi))
                list_curs[topi] = nodej_next
        # postcond: indices 内容和 lengths 一样，因为所有元素都被推进到最后了
        return dummy_head.next

h1 = ListNode(1, ListNode(4, ListNode(5)))
h2 = ListNode(1, ListNode(3, ListNode(4)))
h3 = ListNode(2, ListNode(6))

print(
    Solution().mergeKLists([h1, h2, h3])
)