"""https://leetcode.com/problems/minimum-number-of-operations-to-convert-time.""" # noqa


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def to_number(t: str):
            hour, min = t.split(":")
            res = 60 * int(hour) + int(min)
            return res
        cur_num = to_number(current)
        corr_num = to_number(correct)
        diff = corr_num - cur_num
        count = 0
        re = diff
        while re:
            if re >= 60:
                count += re // 60
                re = re % 60
            elif re >= 15:
                count += re // 15
                re = re % 15
            elif re >= 5:
                count += re // 5
                re = re % 5
            elif re >= 1:
                count += re // 1
                re = re % 1
        return count
