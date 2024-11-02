"""https://leetcode.com/problems/find-the-difference-of-two-arrays"""
from typing import List


class Solution:
    def findDifference(
        self, nums1: List[int], nums2: List[int]
    ) -> List[List[int]]:
        ans1, ans2 = [], []
        h_m1, h_m2 = set(nums1), set(nums2)

        for el in h_m1:
            if el not in h_m2:
                ans1.append(el)

        for el in h_m2:
            if el not in h_m1:
                ans2.append(el)
        return [ans1, ans2]
