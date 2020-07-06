"""1314. Matrix Block Sum
url: https://leetcode.com/problems/matrix-block-sum/
ref: https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
"""
from typing import List


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


if __name__ == "__main__":

    solu = BruteforceSolution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    K = 1
    results = solu.matrixBlockSum(mat, K)
    print(results)
