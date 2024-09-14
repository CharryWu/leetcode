############# 721. Accounts Merge #############
from collections import defaultdict
class Solution():
    def accountsMerge(self, accounts):

        visited_accounts = [False] * len(accounts)
        inverted_map = defaultdict(list) # email => index of account[]
        res = []
        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                inverted_map[email].append(i)
        # DFS code for traversing accounts.
        def dfs(i, emails):
            """
            In each dfs call, populate emails array
            """
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in inverted_map[email]:
                    dfs(neighbor, emails)
        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res
