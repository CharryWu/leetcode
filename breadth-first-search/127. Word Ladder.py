from collections import deque, defaultdict

class Solution:
    def ladderLengthBFS(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Since we're getting MINIMUM transformation needed, use BFS
        """
        if beginWord == endWord:
            return 0
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        mapping = defaultdict(list) # intermediary "c*t" => actual words
        for word in wordset:
            for i in range(len(word)):
                intermediate = word[:i] + '*' + word[i+1:]
                mapping[intermediate].append(word)

        visited = set([beginWord])
        queue = deque([beginWord])
        res = 1 # at least one transformation to reach from beginWord to endWord

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                visited.add(word)

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for neighbor in mapping[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            res += 1
        return 0

    def ladderLengthBFS2(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not wordList or not endWord or endWord not in wordList:
            return 0

        # Since all words are of same length.
        wordlen = len(beginWord)

        all_combo_dict = defaultdict(set)
        for word in wordList:
            for i in range(wordlen):
                intermediate = word[:i] + '*' + word[i+1:]
                all_combo_dict[intermediate].add(word)

        queue = deque()
        queue.append((beginWord, 1))
        visited = set()

        while len(queue) > 0:
            topword, level = queue.popleft()
            if topword == endWord:
                return level
            visited.add(topword)

            for i in range(wordlen):
                intermediate = topword[:i] + '*' + topword[i+1:]
                nxtwords = all_combo_dict[intermediate]

                for nxtword in nxtwords:
                    if nxtword not in visited:
                        queue.append((nxtword, level+1))

        return 0


    def ladderLengthDualWay(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not wordList or not endWord or endWord not in wordList:
            return 0

        # Since all words are of same length.
        wordlen = len(beginWord)

        all_combo_dict = defaultdict(set)
        for word in wordList:
            for i in range(wordlen):
                intermediate = word[:i] + '*' + word[i+1:]
                all_combo_dict[intermediate].add(word)

        queue_top = deque()
        queue_top.append(beginWord)
        visited_top = {
            beginWord: 1
        }

        queue_bottom = deque()
        queue_bottom.append(endWord)
        visited_bottom = {
            endWord: 1
        }

        def visitWord(queue, visited_this, visited_that):
            word = queue.popleft()
            if word in visited_that:
                return visited_this[word] + visited_that[word] - 1

            for i in range(wordlen):
                intermediate = word[:i] + '*' + word[i+1:]
                nxtwords = all_combo_dict[intermediate]
                for nxtword in nxtwords:
                    if nxtword not in visited_this:
                        queue.append(nxtword)
                        visited_this[nxtword] = visited_this[word] + 1
            return None

        res = None
        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while len(queue_top) > 0 and len(queue_bottom) > 0:
            if len(queue_top) <= len(queue_bottom):
                res = visitWord(queue_top, visited_top, visited_bottom)
            else:
                res = visitWord(queue_bottom, visited_bottom, visited_top)
            if res:
                return res
        return 0
