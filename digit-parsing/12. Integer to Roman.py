ROMAN_MAP = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10), 
    ('IX', 9), 
    ('V', 5),
    ('IV', 4),
    ('I', 1),
]

class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        cur_letter = 0

        while num > 0:
            while ROMAN_MAP[cur_letter][1] > num: # 不用担心  cur_letter < len(ROMAN_MAP) 问题，因为最后一个entry是 'I'，num总是能够刚好被消耗完的
                cur_letter += 1
            res.append(ROMAN_MAP[cur_letter][0])
            num -= ROMAN_MAP[cur_letter][1]
        
        return ''.join(res)