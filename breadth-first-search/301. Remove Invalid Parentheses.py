from collections import deque
class Solution:
    def removeInvalidParentheses(self, s):
        """
        Use BFS to guarantee shortest path:
        Starting from the full string, remove one character at each position
        If encounter valid string, don't add to next level
            because we've already found the valid string with min # of removals
        """
        q = deque([s]) # BFS queue contains all substrings with x characters removed, x is current BFS level
        # q: [s], [s[1:], s[0]+s[2:], s[:1]+s[3:], ...], [s[2:], s[]]
        visited = set()
        res = []

        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                if c == ')':
                    if count > 0:
                        count -= 1
                    else: # going negative indicates that some prefix of s has more close than than, invalid
                        return False
            return count == 0

        while q:
            ss = q.popleft()
            if ss in visited:
                continue
            visited.add(ss)
            if isValid(ss):
                res.append(ss)
            elif not res: # Only generate add new BFS level (all substrings has one character removed) if no valid expression has been found.
                # The level is guaranteed to have shortest path (min number of removals from original s)
                for i in range(len(ss)):
                    if ss[i] == ')' or ss[i] == '(':
                        q.append(ss[:i] + ss[i+1:])

        return res
