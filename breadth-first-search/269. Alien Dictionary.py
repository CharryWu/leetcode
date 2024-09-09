"""
Khan's algorithm with cycle detection (summary)
Step 1: Compute In-degree: First we create compute a lookup for the in-degrees of every node. In this particular Leetcode problem, each node has a unique integer identifier, so we can simply store all the in-degrees values using a list where indegree[i] tells us the in-degree of node i.
Step 2: Keep track of all nodes with in-degree of zero: If a node has an in-degree of zero it means it is a course that we can take right now. There are no other courses that it depends on. We create a queue q of all these nodes that have in-degree of zero. At any step of Khan's algorithm, if a node is in q then it is guaranteed that it's "safe to take this course" because it does not depend on any courses that "we have not taken yet".
Step 3: Delete node and edges, then repeat: We take one of these special safe courses x from the queue q and conceptually treat everything as if we have deleted the node x and all its outgoing edges from the graph g. In practice, we don't need to update the graph g, for Khan's algorithm it is sufficient to just update the in-degree value of its neighbours to reflect that this node no longer exists.
This step is basically as if a person took and passed the exam for course x, and now we want to update the other courses dependencies to show that they don't need to worry about x anymore.
Step 4: Repeat: When we removing these edges from x, we are decreasing the in-degree of x's neighbours; this can introduce more nodes with an in-degree of zero. During this step, if any more nodes have their in-degree become zero then they are added to q. We repeat step 3 to process these nodes. Each time we remove a node from q we add it to the final topological sort list result.
Step 5. Detecting Cycle with Khan's Algorithm: If there is a cycle in the graph then result will not include all the nodes in the graph, result will return only some of the nodes. To check if there is a cycle, you just need to check whether the length of result is equal to the number of nodes in the graph, n.
Why does this work?: Suppose there is a cycle in the graph: x1 -> x2 -> ... -> xn -> x1, then none of these nodes will appear in the list because their in-degree will not reach 0 during Khan's algorithm. Each node xi in the cycle can't be put into the queue q because there is always some other predecessor node x_(i-1) with an edge going from x_(i-1) to xi preventing this from happening.
"""

from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        Detecting Cycle with Khan's Algorithm: If there is a cycle in the graph then result will not include all the nodes in the graph,
        result will return only some of the nodes. To check if there is a cycle,
        you just need to check whether the length of result is equal to the number of nodes in the graph, n.
        """
        # Step 1: Create a graph and in-degree count for each character
        graph = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word} # can't use defaultdict(int) because BFS algorithm below adds neighbor if indegree is zero

        # Step 2: Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))

            # Check if the second word is a prefix of the first one (invalid case)
            if word1[:min_len] == word2[:min_len] and len(word1) > len(word2):
                return ""

            # Compare characters in the two words to establish the ordering
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Step 3: Perform topological sort using Kahn's algorithm (BFS)
        zero_in_degree_queue = deque([char for char in in_degree if in_degree[char] == 0])
        result = []

        while zero_in_degree_queue:
            char = zero_in_degree_queue.popleft()
            result.append(char)

            # Decrease the in-degree of adjacent nodes
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_queue.append(neighbor)

        # If we have processed all characters, return the result

        # check for cycle, if
        if len(result) == len(in_degree):
            return "".join(result)
        else:
            return ""
