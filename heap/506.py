"""https://leetcode.com/problems/relative-ranks/"""
import heapq
from typing import List
from utils import run


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = score[:]
        score_m = {score[i]: i for i in range(len(score))}
        score.sort(reverse=True)
        ans = [None] * len(score)

        for i in range(len(score)):
            if i == 0:
                rank = "Gold Medal"
            elif i == 1:
                rank = "Silver Medal"
            elif i == 2:
                rank = "Bronze Medal"
            else:
                rank = str(i+1)
            ans[score_m[score[i]]] = rank
        return ans

    def heapRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        ans = [None] * len(score)
        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))

        place = 1
        while heap:
            _, i = heapq.heappop(heap)
            if place == 1:
                ans[i] = "Gold Medal"
            elif place == 2:
                ans[i] = "Silver Medal"
            elif place == 3:
                ans[i] = "Bronze Medal"
            else:
                ans[i] = str(place)
            place += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {
            "input": {"score": [10, 3, 8, 9, 4]},
            "ans": ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
        }
    ]
    run(test_cases, s.findRelativeRanks)
    run(test_cases, s.heapRelativeRanks)
