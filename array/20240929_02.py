"""你需要寫一個函數，接受一個長度為 N 的字串 S，並回傳將該字串分割成最少子字串所需的最小數量。"""


def solution(S: str):
    last_seen = {}
    substr_count = 0
    start = 0

    for i, char in enumerate(S):
        if char in last_seen and last_seen[char] >= start:
            substr_count += 1
            start = i  # Start a new substring from current index
        last_seen[char] = i  # Update the last seen index of the character

    return substr_count + 1  # Add one for the last substring


# 示例用法
print(solution("abacdec"))  # 輸出: 3
