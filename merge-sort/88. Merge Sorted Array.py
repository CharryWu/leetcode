class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        对于单链表来说，我们直接用双指针从头开始合并即可，但对于数组来说会出问题。
        因为题目让我直接把结果存到 nums1 中，而 nums1 的开头有元素，如果我们无脑复制单链表的逻辑，会覆盖掉 nums1 的原始元素，导致错误。


        但 nums1 后面是空的呀，所以这道题需要我们稍微变通一下：将双指针初始化在数组的尾部，然后从后向前进行合并
        这样即便覆盖了 nums1 中的元素，这些元素也必然早就被用过了，不会影响答案的正确性。
        """
        i, j = m-1, n-1
        p = len(nums1)-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

        # 可能其中一个数组的指针走到尽头了，而另一个还没走完
        # 因为我们本身就是在往 nums1 中放元素，所以只需考虑 nums2 是否剩元素即可
        if j >= 0:
            while i < m:
                nums1[p] = nums2[j]
                j -= 1
                p -= 1
