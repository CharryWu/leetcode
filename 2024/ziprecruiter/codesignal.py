def solution1(diffs):
    num = 1500
    maxx = 1500
    for diff in diffs:
        num += diff
        maxx = max(num, maxx)
    return [maxx, num]

def encode(word):
    bitmap = 0
    for ch in word:
        if ch.islower():
            print()
            bitmap = bitmap | (1 << (ord(ch)-ord('a')))
    return bitmap

def solution2(word, skeletons):
    s = set(word)
    base = encode(s)
    res = []
    for skeleton in skeletons:
        if base == encode(skeleton):
            res.append(skeleton)
    return res

# print(solution2("hello", ["he-lo", "he--o", "-ell-", "hello"])) # ['he-lo', 'hello']


def solution3(matrix):
    m, n = len(matrix), len(matrix[0])
    def avg_top_left(row, col):
        s = 0
        for i in range(row+1):
            for j in range(col+1):
                s += matrix[i][j]

        return s / ((row+1)*(col+1))

    def avg_top_right(row, col):
        s = 0
        for i in range(row+1):
            for j in range(col+1, n):
                s += matrix[i][j]

        return s / ((row+1)*(n-col-1))

    def avg_bottom_left(row, col):
        s = 0
        for i in range(row+1, m):
            for j in range(col+1):
                s += matrix[i][j]

        return s / ((m-row-1)*(col+1))

    def avg_bottom_right(row, col):
        s = 0
        for i in range(row+1, m):
            for j in range(col+1, n):
                s += matrix[i][j]

        return s / ((m-row-1)*(n-col-1))

    diff = float('inf')
    resi, resj = 0, 0

    for i in range(m-1):
        for j in range(n-1):
            tl = avg_top_left(i, j)
            tr = avg_top_right(i, j)
            bl = avg_bottom_left(i, j)
            br = avg_bottom_right(i, j)

            maxx = max([tl, tr, bl, br])
            minn = min([tl, tr, bl, br])
            if maxx-minn < diff:
                print('i=',i,'j=', j, tl, tr, bl, br)
                resi, resj = i, j
                diff = min(diff, maxx-minn)

    return [resi, resj]

matrix = [
    [2,1,1,2],
    [3,2,2,3],
    [3,2,2,3],
    [2,1,1,2]
]

print(solution3(matrix))

matrix = [
    [1,2,3,4,5],
    [4,5,3,4,5],
    [1,2,3,4,5],
    [4,5,3,4,5],
]

print(solution3(matrix))


def solution4(operations):
    saved = []
    res = []
    for operation in operations:
        optype, a, b = operation
        if optype == 0:
            if b > a:
                saved.append((b,a))
            else:
                saved.append((a,b))

        elif optype == 1:
            ww, hh = a, b
            if hh > ww:
                ww, hh = hh, ww
            found = True
            for w, h in saved:
                if ww <= w and hh <= h:
                    found = True
                    res.append(True)
                    break
            if not found:
                res.append(False)
    return res





