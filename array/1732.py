from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_alt = max_alt = 0
        for ga in gain:
            cur_alt = cur_alt + ga
            max_alt = max(max_alt, cur_alt)
        return max_alt
