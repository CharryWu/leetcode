class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        y = 0 # y 是 x 翻转后的数字。比较 y == x 就可以知道x是不是回文数字了
        while temp > 0:
            last_num = temp % 10
            temp //= 10
            y = y * 10 + last_num
        
        return y == x
