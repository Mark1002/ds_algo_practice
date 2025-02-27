"""https://leetcode.com/problems/evaluate-division."""
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:
        graphs = defaultdict(list)
        edges = dict()
        # 建立 undirected graph
        for i, equation in enumerate(equations):
            a, b = equation[0], equation[1]
            graphs[a].append(b)
            graphs[b].append(a)
            # 發現equations的value反向為導數關係
            edges[(a, b)] = values[i]
            edges[(b, a)] = 1 / values[i]

        def dfs(s: str, e: str, seen: set) -> float:
            seen.add(s)
            # 找到最後一段edge立馬回傳
            if (s, e) in edges:
                return edges[(s, e)]
            for n in graphs[s]:
                # 走過了就pass
                if n in seen:
                    continue
                # 觀察範例得知遞移為相乘關係
                ans = edges[(s, n)] * dfs(n, e, seen)
                if ans > 0:
                    return ans
            # 如果都找不到對應的edge最後一律回傳-1
            return -1
        return [dfs(s, e, set()) for s, e in queries]
