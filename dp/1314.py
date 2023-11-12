"""1314. Matrix Block Sum
url: https://leetcode.com/problems/matrix-block-sum/
ref: https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
"""
from typing import List
from utils import timer


class BruteforceSolution:
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        return [
            [self.cum_sum(i,j, K, mat) for j in range(n)] for i in range(m)
        ]
    
    def cum_sum(self, i,j, K, mat):
        cors = []
        for r in range(i-K, i+K+1):
            if r < 0 or r > len(mat)-1:
                continue
            for c in range(j-K, j+K+1):
                if c < 0 or c > len(mat[i])-1:
                    continue
                cors.append((r,c))
        return sum([mat[r][c] for r,c in cors])

class DPSolution:
    
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])    
        range_sum = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                range_sum[i+1][j+1] = range_sum[i+1][j] + range_sum[i][j+1] - range_sum[i][j] + mat[i][j]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i-K), max(0, j-K), min(m, i+K+1), min(n, j+K+1)
                ans[i][j] = range_sum[r2][c2] - range_sum[r1][c2] - range_sum[r2][c1] + range_sum[r1][c1]
        return ans

@timer
def execute_brute():
    solu = BruteforceSolution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    K = 1
    results = solu.matrixBlockSum(mat, K)
    print(results)

@timer
def execute_dp():
    solu = DPSolution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    K = 1
    results = solu.matrixBlockSum(mat, K)
    print(results)


if __name__ == "__main__":
    # execute_brute()
    execute_dp()
