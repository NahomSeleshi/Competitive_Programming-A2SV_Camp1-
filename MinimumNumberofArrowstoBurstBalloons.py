class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        
        index = 0
        minimumArrows = 0
        while index < len(points):
            
            end = points[index][1]
            while index < len(points) and end >= points[index][0]:
                if end > points[index][1]:
                    end = points[index][1]
                index += 1
       
            minimumArrows += 1
        
        return minimumArrows

                    
