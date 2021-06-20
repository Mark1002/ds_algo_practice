"""
15. 3Sum
url: https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = {}
        nums.sort()
        print(nums)
        for j in range(len(nums)):
            if j > 0 and nums[j] == nums[j-1]: # to prevent the same x, because the same x get the same target (y + z) value
                continue
            x_i = j
            target = nums[x_i] * -1
            d = {}
            for i in range(len(nums)):
                if i == x_i:
                    continue
                if d.get(target-nums[i]):
                    x = nums[x_i]
                    y = nums[i]
                    z = nums[d[target-nums[i]]]
                    result = sorted([x,y,z])
                    print((j, result))
                    results[str(result)] = result
                else:
                    d[nums[i]] = i
        return list(results.values())

def main():
    s = Solution()
    results = s.threeSum([-1,-1, 2])
    print(results)

if __name__ == '__main__':
    main()
