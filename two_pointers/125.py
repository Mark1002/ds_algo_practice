"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    test_cases = [
        {"input": "@@a@@_b_a_", "ans": True},
        {"input": "A man, a plan, a canal: Panama", "ans": True},
        {"input": " ", "ans": True},
        {"input": "race a car", "ans": False}
    ]
    for test_case in test_cases:
        assert s.isPalindrome(test_case["input"]) == test_case["ans"]
