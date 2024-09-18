class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = 0
        ages.sort()
        for i in range(len(ages)):
            a = ages[i]
            right = bisect.bisect_right(ages, a)
            left = bisect.bisect_right(ages, 0.5 * a + 7)
            cnt += max(0, right - left - 1)
        return cnt
