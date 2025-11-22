"""https://leetcode.com/problems/find-if-path-exists-in-graph."""

from typing import List
from collections import deque
from utils import run

class Solution:
    def validPath_iterate_dfs(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        visit = set()
        stack = [source]
        visit.add(source)

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        while stack:
            p = stack.pop()
            if p == destination:
                return True
    
            for ni in graph[p]:
                if ni not in visit:
                    stack.append(ni)
                    visit.add(ni)
        return False

    def validPath_recursive_dfs(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visit = set()
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node) -> bool:
            """Func execution means pop from stack."""
            if node == destination:
                return True
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    if dfs(nei):
                        return True
            return False

        return dfs(source)

    def validPath_bfs(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()
        queue = deque()
        queue.append(source)
        visit.add(source)

        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for nie in graph[curr]:
                if nie in visit:
                    continue
                queue.append(nie)
                visit.add(nie)
        return False


if __name__ == "__main__":
    
    test_cases = [
        {
            "input": {
                "n": 3,
                "edges": [[0, 1], [1, 2], [2, 0]],
                "source": 0,
                "destination": 2
            },
            "ans": True
        },
        {
            "input": {
                "n": 6,
                "edges": [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
                "source": 0,
                "destination": 5
            },
            "ans": False
        },
        {
            "input": {
                "n": 1,
                "edges": [],
                "source": 0,
                "destination": 0
            },
            "ans": True
        },
        {
            "input": {
                "n": 10,
                "edges": [[0, 7], [0, 8], [6, 1], [2, 0], [0, 4], [5, 8], [4, 7], [1, 3], [3, 5], [6, 5]],
                "source": 7,
                "destination": 5
            },
            "ans": True
        }
    ]
    
    solution = Solution()
    run(test_cases, solution.validPath_iterate_dfs)
    run(test_cases, solution.validPath_recursive_dfs)
    run(test_cases, solution.validPath_bfs)

