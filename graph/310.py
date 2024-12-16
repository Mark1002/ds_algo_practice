"""https://leetcode.com/problems/minimum-height-trees"""
from collections import deque
from typing import List, Dict


class Solution:
    def findMinHeightTreesBFS(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        if n == 1:
            return [0]

        # construct adjacency lists
        hm = {i: [] for i in range(n)}
        for edge in edges:
            s, e = edge
            hm[s].append(e)
            hm[e].append(s)

        # add degree 1 leaf node
        q = deque([k for k in hm if len(hm[k]) == 1])
        remain_count = n
        #  MHTs can a graph have at most 2
        while remain_count > 2:
            leaf_count = len(q)
            remain_count -= leaf_count
            for _ in range(leaf_count):
                # remove leaf node
                leaf = q.popleft()
                ref = hm[leaf].pop()
                hm[ref].remove(leaf)

                if len(hm[ref]) == 1:
                    q.append(ref)
        return list(q)

    def findMinHeightTreesDFS(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        """DFS will be timeout, O(n^2)."""
        def dfs(i, seen: set, hm: Dict[int, List[int]]) -> int:
            seen.add(i)
            h = 0
            for el in hm[i]:
                if el in seen:
                    continue
                h = max(h, dfs(el, seen, hm))
            return h+1

        hm = {i: [] for i in range(n)}
        for edge in edges:
            s, e = edge
            hm[s].append(e)
            hm[e].append(s)

        result = []
        min_h = float("inf")
        for i in range(n):
            seen = set()
            cur_h = dfs(i, seen, hm)
            if cur_h < min_h:
                min_h = cur_h
                result = [i]
            elif cur_h == min_h:
                result.append(i)
        return result
