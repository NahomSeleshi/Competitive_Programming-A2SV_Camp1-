class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        BFSPossiblePaths = deque([0])
        far = 0
        while BFSPossiblePaths:
            node = BFSPossiblePaths.popleft()
            if node == len(s)-1: return True
            
            #update our small jump with the new far so that we 
            #don't iterate over the same range again
            smallJump = max(far+1, node + minJump)
            bigJump = min(node+maxJump, len(s)-1)
            for index in range(smallJump, bigJump+1):
                if s[index] == '0': 
                    BFSPossiblePaths.append(index)
            far = node + maxJump
        return False
    
