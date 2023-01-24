"""
Initialize a list result which will return the Gray code sequence for the value of n.

Use a recursive helper function grayCodeHelper and pass the result list as a reference.

At base condition (n = 0) add the number 0 to result and return. This is because the Gray code sequence starts with 0.

As demonstrated in the intuition section, we can derive the sequence for n from the sequence for n - 1. So make a recursive call to grayCodeHelper function with n - 1.

Set the bit at (n−1)th(n - 1)^{th}(n−1) 
th
  position and assign it to a variable mask. mask is used to set the (n−1)th(n - 1)^{th}(n−1) 
th
  bit from the least significant bit (LSB) of all the numbers present in the current list result.

Iterate backward over the result list.

Set the (n−1)th(n - 1)^{th}(n−1) 
th
  bit of the ithi^{th}i 
th
  number and add the new number formed to the result list. Thus, the size of the result list will double.

The result list contains a valid Gray code sequence for the current given number of bits. Return the result list.
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []

        def grayCodeHelper(n):
            nonlocal res
            if n == 0:
                res.append(0)
                return
            grayCodeHelper(n-1)
            mask = 1 << (n-1)
            for i in range(len(res)-1, -1, -1):
                newnum = mask | res[i]
                res.append(newnum)
    
        grayCodeHelper(n)
        return res

    def grayCode2(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            prev_len = len(res)
            mask = 1 << (i-1)
            for j in range(prev_len-1, -1, -1):
                newnum = mask | res[j]
                res.append(newnum)
        return res
