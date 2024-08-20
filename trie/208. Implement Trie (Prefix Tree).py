class PrefixTreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        """
        This code inserts a word into a Trie data structure.
        It iterates through each character in the word,
        creating a new node in the Trie if the character doesn't already exist,
        and marks the end of the word when all characters have been processed.

        Args:
        - word (str): The word to be inserted.

        Returns:
        - None
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = PrefixTreeNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the trie.

        Args:
        - word (str): The word to be searched.

        Returns:
        - bool: True if the word is found in the trie, False otherwise.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
