from typing import *
class Codec:
    def encode(self, strs: List[str]) -> str:
        """
        Encode format: 4#abcd3#abc2#ab
        """
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s): # read input character by character
            j = i # end of delimiter
            while s[j] != '#': # go all the way to pound sign
                j += 1
            length = int(s[i:j]) # str[i:j] is length of next word
            res.append(s[j+1:j+1+length])
            i = j+1+length # beginning of next encoded string
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
