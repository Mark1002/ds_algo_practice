"""https://leetcode.com/problems/keys-and-rooms."""
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(open_rooms, keys):
            for key in keys:
                if open_rooms[key]:
                    continue
                open_rooms[key] = True
                dfs(open_rooms, rooms[key])
        open_rooms = [False] * len(rooms)
        open_rooms[0] = True
        dfs(open_rooms, rooms[0])
        return all(open_rooms)
