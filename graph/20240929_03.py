"""
請實作一個函式，給定一個正整數 N {1...N} 表示無向圖各個端點
以及兩個長度為 M 的正整數陣列 A 和 B，兩個陣列，兩端點之間的邊表示(A[K], B[K])
回傳能使所有邊的端點值總和最大化的結果。
"""


def solution(N, A, B):
    from collections import defaultdict

    # Create a dictionary to count the degree of each vertex
    degree = defaultdict(int)

    # Count the degree of each vertex based on edges
    for a, b in zip(A, B):
        degree[a] += 1
        degree[b] += 1

    # Create a list of degrees and sort it in descending order
    degree_list = sorted(degree.values(), reverse=True)

    # Assign values from N to 1 based on the sorted degree list
    max_sum = 0
    value = N
    for d in degree_list:
        if d > 0:  # Only consider vertices that have edges
            max_sum += value * d
            value -= 1

    return max_sum


# Example usage:
print(solution(5, [2, 2, 1, 2], [1, 3, 4, 4]))  # Output: 31
print(solution(3, [1], [3]))                      # Output: 5
print(solution(4, [1, 3], [2, 4]))               # Output: 10
