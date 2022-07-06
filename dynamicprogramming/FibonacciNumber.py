class Solution:
    def fib(self, n: int) -> int:
        memo = [0] * (n + 1)
        if n < 2:
            return n
        memo[0] = 0
        memo[1] = 1
        for i in range(2, n + 1, 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(2))
    print(solution.fib(3))
