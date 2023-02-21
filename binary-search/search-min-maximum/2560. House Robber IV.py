class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        Here we want to minimize the maximum house we steal.
        So it's not a robber-like problem,
        it's actually a mini-max problem.

        When we mini-max one capacity to do something,
        (here is robber k houses)
        we can use bianry search.

        Binary search the minimum capability of the robber
        to steal at least k houses.

        Given 1 <= A[i] <= 1e9,
        we can initial the binary search range as
        left = 1 and right = 1e9.
        we can also set left = min(A) and right = max(A).

        Assume the capability is mid,
        we iterate the houses A,
        and greedily take the houses as many as possible,
        if mid > A[i] and we didn't take A[i-1].

        Then we check if we have take k houses,
        If take >= k,
        we have big enough capability,
        right = mid.
        If take < k,
        we don't have big enough capability,
        left = mid + 1.

        Finally we return the binary search result.
        """

        l, r = min(A), max(A)
        while l < r:
            m = (l + r) // 2
            last = take = 0
            for a in A:
                if last:
                    last = 0
                    continue
                if a <= m:
                    take += 1
                    last = 1
            if take >= k:
                r = m
            else:
                l = m + 1
        return l