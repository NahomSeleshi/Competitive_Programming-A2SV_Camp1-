from math import inf
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
        def DP(row, column):
            if row == len(grid)-1 and column == len(grid[0])-1:
                return grid[row][column]
            if memo[row][column] != -1: 
                return memo[row][column]
            
            rightPath = inf
            downPath = inf
            if row < len(grid)-1:
                downPath = DP(row+1, column)
            if column < len(grid[0])-1:
                rightPath = DP(row, column+1)
                
            currentMin = min(downPath, rightPath)
            memo[row][column] = currentMin + grid[row][column]
            return currentMin + grid[row][column]
        
        return DP(0,0)
            
