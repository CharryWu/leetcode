# You are given a chat message msg, and a list of stop words `w`, find the start offset index of a sequence of characters in `msg` that includes all the words in `w` in any order without any other character. If there’s no such sequence, return -1.  For example:

# W = [“foo”, “bar”, "xyz"]

# msg1=”how are you barfoo?”
# answer1=12

# msg2=”how are you foobar?”
# answer2=12

# msg3=”how are you fooba?”
# answer3=-1


# W = [“a”, “b”, "c"] => abc, acb, bac, bca, cab, cba

# msg1=”xyz abc?”
# answer1=12


# msg2=”how are you cba?”
# answer2=12

# msg3=”how are you cb?”
# answer3=-1

def solution(W, msg: str):
    n = len(W)
    permutations = []

    def backtrack(path, i):
        if i == n:
            permutations.append(''.join(path))

        for j in range(i+1, n):
            W[j], W[i] = W[i], W[j]
            path.append(W[j])
            backtrack(path, j)
            path.pop()

            W[j], W[i] = W[i], W[j]

            # path.append(W[j])
            # backtrack(path, j)
            # path.pop()

        return


    backtrack([], 0)
    # postcond: words is the list of permutations of w
    print(permutations)

    for p in permutations:
        idx = msg.index(p)
        if idx >= 0:
            return idx

    return -1

solution(['a', 'b', 'c'], 'xyz abc?')

