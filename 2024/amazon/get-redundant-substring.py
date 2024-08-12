from collections import defaultdict
vowels = set('aeiou')


def getRedundantSubstrings(word, a, b):
    score_map = {} # map from score to position list [i1, i2, i3]

    # current_score = 0
    # for i, c in enumerate(word):



# Example usage
word = "abbacc"
a = -1
b = 2
result = getRedundantSubstrings(word, a, b)
print(result)  # Output should be 5

# Example usage
word = "akljfs"
a = -2
b = 1
result = getRedundantSubstrings(word, a, b)
print(result)  # Output should be 15
