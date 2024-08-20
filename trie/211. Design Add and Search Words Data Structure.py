class Node:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.children[i]:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.end = True

    def searchAt(self, startNode, word) -> bool:
        if not word:
            return startNode.end
        topc = word[0]
        if topc == '.':
            for child in startNode.children:
                if child and self.searchAt(child, word[1:]):
                    return True
        else:
            idx = ord(topc) - ord('a')
            if not startNode.children[idx]:
                return False
            return self.searchAt(startNode.children[idx], word[1:])
        return False

    def search(self, word: str) -> bool:
        if word == "":
            return self.root.end
        return self.searchAt(self.root, word)
