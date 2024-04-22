class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left, right = 0, len(num)-1
        while left <= right:
            if num[left] == num[right] and (num[left] not in '018'):
                return False
            if num[left] != num[right]:
                valid = False
                if num[left] == '6' and num[right] == '9':
                    valid = True
                elif num[left] == '9' and  num[right] == '6':
                    valid = True
                if not valid:
                    return False
            left += 1
            right -= 1

        if left < right:
            return False
        return True
