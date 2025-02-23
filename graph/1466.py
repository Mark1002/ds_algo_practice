"""https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero.""" # noqa
from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        direct_edge = set()
        # construct undirected graph
        for s, e in connections:
            graph[s].append(e)
            graph[e].append(s)
            # record all the direct edge
            direct_edge.add((s, e))

        reverse_count = 0
        seem = set()
        stack = [0]
        while stack:
            cur = stack.pop()
            print(cur)
            seem.add(cur)
            for nxt in graph[cur]:
                if nxt in seem:
                    continue
                # if the path is from origin counter add 1
                if (cur, nxt) in direct_edge:
                    reverse_count += 1
                stack.append(nxt)
        return reverse_count
