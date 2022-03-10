class Solution:
    def fib(self, n: int) -> int:
        memo = [False for values in range(n+1)]
        def DP(index):
            if index == 0:
                memo[index] == 0
                return 0
            if index == 1:
                memo[index] == 1
                return 1
            if memo[index]: 
                return memo[index]
            currentFib = DP(index-1) + DP(index - 2)
            memo[index] = currentFib
            return currentFib
        return DP(n)
        
        
