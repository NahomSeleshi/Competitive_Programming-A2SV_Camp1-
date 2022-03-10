class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentMaximumPrice = prices[len(prices)-1]
        finalProfit = 0
        
        for i in range(len(prices)-1, -1, -1):
            currentProfit = currentMaximumPrice - prices[i]
            currentMaximumPrice = max(currentMaximumPrice, prices[i])
            finalProfit = max(currentProfit, finalProfit)
                
        return finalProfit if finalProfit > 0 else 0
            
            
        
