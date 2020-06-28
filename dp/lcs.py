"""Longest Common Subsequence.

ref: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

"""


def recur_lcs(l1: str, l2: str) -> int:
    """Recursion Lcs."""
    m, n = len(l1), len(l2)
    if m == 1 or n == 1:
        return 1
    if l1[-1] == l2[-1]:
        return recur_lcs(l1[:m-1], l2[:n-1]) + 1
    else:
        return max(recur_lcs(l1[:m-1], l2[:n]), recur_lcs(l1[:m], l2[:n-1]))


def dp_lcs(l1: str, l2: str) -> int:
    """Dp for lcs."""
    m, n = len(l1), len(l2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if l1[i-1] == l2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]


if __name__ == "__main__":
    l1 = "AGGTAB"
    l2 = "GXTXAYB"
    length = recur_lcs(l1, l2)
    print(f'length: {length}')
    length = dp_lcs(l1, l2)
    print(f'length: {length}')
