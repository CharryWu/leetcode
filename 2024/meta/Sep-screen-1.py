#Question 1. Given a binary tree root node, write a function that returns the tree diameter
#definition: diameter of a tree is the number of nodes on the longest path between any two nodes
#example
            1
          /   \
         2     3
        /     / \
       4     5   6
                  \
                   7


            1
             \
              3
             / \
            5   6
                  \
                   7

#ans = 6

def solution(root):
    res = 0

    def dfs(node):
        nonlocal res
        if not node:
            return 0
        leftres = dfs(node.left)
        rightres = dfs(node.right)
        s = leftres + rightres + 1
        res = max(res, s)

        return 1+max(leftres, rightres)

    dfs(root)
    return res


dfs(1): res = 1 + 2 + 3 = 6, => 1 + 3 = 4
    - dfs(2): res = 1 + 1 + 0 = 2, => 2
        - dfs(4) => 1 + 0 = 1, res = 1
        - dfs(None) => 0

    - dfs(3): res = 1 + 1 + 2 = 4, => 3
        - dfs(5) => 1
        - dfs(6) => 2
            - dfs(7) => 1


#Question 2. Given a matrix of integers print out its values along the diagonals that move in the top right to bottom left direction. Each diagonal goes down and to the left as shown in the example. There should be newlines between each diagonal.
#example
[[1,  2,  3,  4],
 [5,  6,  7,  8],
 [9, 10, 11, 12]]

1  (0, 0) sum = 0
2 5  (0, 1), (1, 0) sum = 1
3 6 9 (0, 2), (1,1) (2, 0) = sum = 2
4 7 10 sum = 4
8 11  sum = 5
12  = sum = 6



3 6 9 (0, 2), (1,1) (2, 0) = sum = 2
i, j
0, 2
1, 1
2, 0


for i in range(m):
    for j in range(n):


# for s in range(m+n):
#     for i in range(m):
#         for j in range():
def solution(matrix):
    rows, cols = len(matrix), len(matrix[0])

    for col in range(cols):
        i, j = 0, col

        while i < rows and j >= 0:
            print(matrix[i][j], end=' ')
            i += 1
            j -= 1


    for row in range(1, rows):
        i, j = row, cols-1

        while i < rows and j >= 0:
            print(matrix[i][j], end=' ')
            i += 1 # same, move bottom left
            j -= 1

solution(
    [[1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]]
)

rows = 3, cols = 4

col = 0
i, j = 0, 0
print 1

col = 1
i, j = 0, 1
print(2), i+=1 = 1, j -= 1, 0
i, j = 1, 0
print(5)


col = 2
i, j = 0, 2
print(3),
i, j = 1, 1
print(6)
i, j = 2, 0
print(9)



col = 3
i, j = 0, 3
print(4),
i, j = 1, 2
print(7)
i, j = 3, 0
print(10)


row = 1
i, j = 1, 3
print(8),
i, j = 2, 2
print(11)

row = 2
i, j = 2, 3
print(12),
