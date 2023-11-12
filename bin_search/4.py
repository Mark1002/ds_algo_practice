"""
url: https://leetcode.com/problems/median-of-two-sorted-arrays
"""

from typing import List


class Solution:
    """Not passed."""
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 or len(nums2) == 0:
            merge_nums = nums1 + nums2
        elif nums1[-1] <= nums2[0]:
            merge_nums = nums1 + nums2
        elif nums2[-1] <= nums1[0]:
            merge_nums = nums2 + nums1
        else:
            sub_nums1 = self.sub_median(nums1)
            sub_nums2 = self.sub_median(nums2)
            merge_nums = sorted(sub_nums1 + sub_nums2)
        mid_idx = len(merge_nums) // 2
        if len(merge_nums) % 2 == 0:
            return (merge_nums[mid_idx-1] + merge_nums[mid_idx]) / 2
        else:
            return merge_nums[mid_idx]

    def sub_median(self, array: List[int]) -> List[int]:
        mid_idx = len(array) // 2
        if len(array) % 2 == 0:
            sub_nums = array[mid_idx-1:mid_idx+1]
        else:
            sub_nums = [array[mid_idx]]
        return sub_nums


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"nums1": [1, 2, 55], "nums2": [33, 66]},
        {"nums1": [1, 3], "nums2": [2]},
        {"nums1": [1, 2], "nums2": [3, 4]},
        {"nums1": [33, 34, 65, 66], "nums2": [40, 41, 42]},
        {"nums1": [1], "nums2": [2, 3, 4]},
        {"nums1": [], "nums2": [2, 3, 4]},
        {"nums1": [78, 79, 80, 88], "nums2": []},
    ]
    for test_case in test_cases:
        print(s.findMedianSortedArrays(test_case["nums1"], test_case["nums2"]))
