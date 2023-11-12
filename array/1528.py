"""
1528. Shuffle String
url: https://leetcode.com/problems/shuffle-string/
"""
from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = [None] * len(s)
        for i, j in enumerate(indices):
            t[j] = s[i]
        return ''.join(t)

def main():
    """Main."""
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    result = Solution().restoreString(s, indices)
    print(result)

if __name__ == "__main__":
    main()
