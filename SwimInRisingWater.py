from heapq import heappop, heappush
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap, leastTime = [(grid[0][0],0,0)], grid[0][0]
        visited = [[False for i in range(len(grid[0]))]for j in range(len(grid))]
        visited[0][0] = True
        while minHeap:
            node = heappop(minHeap)
            time, row, column = node
            leastTime = max(leastTime, time)
            if row > 0 and not visited[row-1][column]:
                visited[row - 1][column] = True
                heappush(minHeap, (grid[row-1][column], row-1, column))
            if row < len(grid)-1 and not visited[row + 1][column]:
                visited[row + 1][column] = True
                heappush(minHeap,(grid[row + 1][column], row + 1, column))
            if column > 0 and not visited[row][column-1]:
                visited[row][column - 1] = True
                heappush(minHeap,(grid[row][column - 1], row, column-1))
            if column< len(grid[0])-1 and not visited[row][column+1]:
                visited[row][column + 1] = True
                heappush(minHeap,(grid[row][column + 1], row , column + 1))
            if row == len(grid)-1 and column == len(grid[0])-1: return leastTime
