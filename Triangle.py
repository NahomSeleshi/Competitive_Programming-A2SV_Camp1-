class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # initialize all the values of memo to a number smaller than the constraint so that 
        # I can save zeros as path sums otherwise, "if memo[i][j]:" wouldn't work as a base case
        # because 0 can be stored as path sum and memo[i][j] = 0 is treated as false so no memoization
        memo = [[-100000 for column in range(len(triangle))] for row in range(len(triangle))]
        
        # row is a list of numbers
        def DFS(row, rowNum, i):
            
            if rowNum == len(triangle)-1:
                return row[i]
            if memo[rowNum][i] != -100000:
                return memo[rowNum][i]
            
            currentMinimum = min(DFS(triangle[rowNum+1], rowNum+1, i), DFS(triangle[rowNum+1], rowNum+1, i+1))
            minimumPathSum = triangle[rowNum][i] + currentMinimum
            memo[rowNum][i] = minimumPathSum
            return minimumPathSum
                
        return DFS(triangle[0], 0, 0)
        
