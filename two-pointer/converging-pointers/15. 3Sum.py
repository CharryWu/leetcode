class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            """
            Each loop focus on first/smallest number in the triplet, try to find two sum = 0 - first number
            using two pointer in sorted array
            """
            if num > 0: # will never reach zero sum by adding three positive integers!
                break

            if i >= 1 and num == nums[i-1]: # skip same number, res shouldn't include duplicate triplets
                continue

            l, r = i + 1, len(nums)-1 # sorted two sum for the rest of array, use two pointer method

            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1 # only have to update one pointer, the other point can be updated by
                    # two "if"s above
                    while nums[l] == nums[l-1] and l < r: # don't want to have same sum
                        l += 1

        return res
