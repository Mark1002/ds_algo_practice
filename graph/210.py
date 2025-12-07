"""https://leetcode.com/problems/course-schedule-ii/"""
from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """topological sort Kahn's algorithm (BFS)."""
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for v, u in prerequisites:
            # u -> v
            graph[u].append(v)
            indegree[v]+=1
        
        q = deque([i for i in range(numCourses) if indegree[i]==0])
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indegree[v]-=1
                if indegree[v] == 0:
                    q.append(v) 

        return order if len(order) == numCourses else []