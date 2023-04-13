# 全局变量，记录递归函数的递归层数
count = 0

# 输入 n，打印 n 个 tab 缩进
def printIndent(n):
    for i in range(n):
        print("   ", end =" ")

"""
count = 0

def printIndent(n):
    for i in range(n):
        print("   ", end='')

def dp(ring, i, key, j, charToIndex):
    global count
    # printIndent(count)
    # print("i = %d, j = %d" % (i, j))

    if j == len(key):
        # count -= 1
        # printIndent(count)
        # print("return 0")
        return 0

    res = float('inf')
    for k in charToIndex[key[j]]:
        d = abs(k - i)
        minDist = min(d, len(ring) - d)
        res = min(res, minDist + dp(ring, k, key, j + 1, charToIndex))

    # count -= 1
    # printIndent(count)
    # print("return %d" % res)
    return res
"""