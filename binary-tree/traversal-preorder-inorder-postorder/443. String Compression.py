from collections import deque
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        char = chars[0]
        rp, wp = 1, 0
        def writeDigits(count):
            nonlocal wp
            digits = deque([])
            while count > 0:
                digits.appendleft(count%10)
                count //= 10
            for digit in digits:
                chars[wp] = str(digit)
                wp += 1
            
        while rp < len(chars):
            if chars[rp] == chars[rp-1]:
                count += 1
            else:
                chars[wp] = char
                wp += 1
                if count > 1:
                    writeDigits(count)
                char = chars[rp]
                count = 1
            rp += 1
        
        if count > 0:
            chars[wp] = char
            wp += 1
            if count > 1:
                writeDigits(count)
        return wp