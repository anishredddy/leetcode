from typing import List

MOD = 10**9 + 7  # Define the modulo as per the problem requirement

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        counts_0 = [0] * 26  # Initial counts of each character in the string

        # Build the initial counts vector
        for c in s:
            ind = ord(c) - ord('a')
            counts_0[ind] += 1

        # Build the transition matrix T
        T = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for k in range(1, nums[i] + 1):
                j = (i + k) % 26
                T[i][j] += 1

        def mat_mul(A, B):
            n = len(A)
            m = len(A[0])
            p = len(B[0])
            result = [[0] * p for _ in range(n)]
            for i in range(n):
                for j in range(p):
                    total = 0
                    for k in range(m):
                        total = (total + A[i][k] * B[k][j]) % MOD
                    result[i][j] = total
            return result

        def mat_pow(mat, power):
            # Initialize result as the identity matrix
            result = [[int(i == j) for j in range(len(mat))] for i in range(len(mat))]
            while power > 0:
                if power % 2 == 1:
                    result = mat_mul(result, mat)
                mat = mat_mul(mat, mat)
                power //= 2
            return result

        # Raise the transition matrix to the power t
        T_power_t = mat_pow(T, t)

        # Multiply the initial counts vector with T^t
        counts_0_mat = [counts_0]  # Convert counts_0 to a 1x26 matrix
        counts_t_mat = mat_mul(counts_0_mat, T_power_t)
        counts_t = counts_t_mat[0]  # Extract the list from the 1x26 matrix

        # Calculate the total length after t transformations
        total_length = sum(counts_t) % MOD

        return total_length
