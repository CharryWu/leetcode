def encode(c): #haystack and needle consist of only lowercase English characters.
    return ord(c)-ord('a')

# Robin-Karp 算法
class Solution:
    def strStr(self, txt: str, pat: str) -> int:
        L = len(pat)
        R = 26
        RL = R ** (L-1)
        window_hash = 0
        pat_hash = 0
        
        txt_encoded = list(map(encode, txt))
        
        for pc in pat:
            pat_hash = R*pat_hash + encode(pc)
            
        left, right = 0, 0
        while right  < len(txt):
            rnum = txt_encoded[right]
            window_hash = R*window_hash + rnum
            right += 1
            
            if right-left == L:
                if pat_hash == window_hash:
                    return left
                lnum = txt_encoded[left]
                window_hash -= lnum*RL
                left += 1
        
        return -1
