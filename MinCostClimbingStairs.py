from math import inf
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo  = [0 for i in range(len(cost))]
        def dp(index):
            if index+2 >= len(cost): 
                memo[index] = cost[index]
                return cost[index]
            if memo[index]: 
                return memo[index]
            cost1, cost2 = inf, inf
            cost1 = cost[index] + dp(index + 1)
            if index + 2 <= len(cost)-1:
                cost2 = cost[index] + dp(index + 2)  
            currentCost = min(cost1, cost2)
            memo[index] = currentCost
            return currentCost
        return min(dp(0), dp(1))
