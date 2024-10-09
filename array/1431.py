"""https://leetcode.com/problems/kids-with-the-greatest-number-of-candies"""
from typing import List


class Solution:
    def kidsWithCandies(
        self, candies: List[int], extraCandies: int
    ) -> List[bool]:
        results = []
        max_candy = max(candies)
        for candy in candies:
            if (candy + extraCandies) >= max_candy:
                results.append(True)
            else:
                results.append(False)

        return results
