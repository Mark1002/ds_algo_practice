"""
url: https://leetcode.com/problems/longest-palindromic-substring/
"""


class BruceFroceSolution:
    def longestPalindrome(self, s: str) -> str:
        long_s = s[0]
        for i in range(len(s)):
            for j in range(len(s)):
                cur_s = self.searhPalindrome(s[i:j+1])
                if len(long_s) < len(cur_s):
                    long_s = cur_s
        return long_s

    def searhPalindrome(slef, s: str):
        i, j = 0, len(s)-1
        l, r = i, j
        while i <= j:
            if s[i] != s[j]:
                l, r = i+1, j-1
                if l >= r:
                    l, r = 0, 0
            i += 1
            j -= 1
        return s[l:r+1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        以外層回圈每次字元當中心點，往左右擴張
        """
        res = ""
        res_len = 0
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
            # even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                l -= 1
                r += 1
        return res

if __name__ == "__main__":
    test_cases = [
        {"input": "babad", "expected": "bab"},
        {"input": "cbbd", "expected": "bb"},
        {"input": "ab", "expected": "b"},
        {"input": "abcdef", "expected": "a"},
        {"input": "s7sd", "expected": "s7s"},
        {"input": "abb", "expected": "bb"},
    ]
    # s = BruceFroceSolution()
    s = Solution()
    for test_case in test_cases:
        output = s.longestPalindrome(test_case["input"])
        print(output)
        # assert output == test_case["expected"]
