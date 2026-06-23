class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp.reverse()
            res = 0
            for j in range(m):
                dp[j], res = res, (res + dp[j]) % MOD

        res = 0
        for d in dp:
            res = (res + d) % MOD

        return (res << 1) % MOD