"""https://leetcode.com/problems/find-the-town-judge."""
from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judge_count = n-1
        # init indegree and outdegree counter 
        indeg = defaultdict(int)
        outdeg = defaultdict(int)
        for u, v in trust:
            outdeg[u]+=1
            indeg[v]+=1

        for i in range(1, n+1):
            if indeg[i] == judge_count and outdeg[i] == 0:
                return i
        return -1
