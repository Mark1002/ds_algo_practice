from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  # cur char index
        ans = 0  # cur compressed array length
        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            # assign compressed array letter
            chars[ans] = letter
            ans += 1
            # add dight when count > 1
            if count > 1:
                for d in str(count):
                    chars[ans] = d
                    ans += 1
        return ans
