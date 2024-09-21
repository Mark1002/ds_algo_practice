"""https://leetcode.com/problems/maximum-product-subarray."""
from typing import List


class Solution:
    """https://anj910.medium.com/leetcode-152-maximum-product-subarray-%E4%B8%AD%E6%96%87-38bc1e224017""" # noqa
    def maxProduct(self, nums: List[int]) -> int:
        # Need to maintain max and min product
        # Becasue two negative product would become positive
        res = max_pro = min_pro = nums[0]
        for num in nums[1:]:
            # Swap can make negative min product more min
            # and may be positive in the future.
            # Max product would awlays be replaced by cur negative num
            if num < 0:
                max_pro, min_pro = min_pro, max_pro
            max_pro = max(max_pro * num, num)
            min_pro = min(min_pro * num, num)
            res = max(res, max_pro)
        return res
