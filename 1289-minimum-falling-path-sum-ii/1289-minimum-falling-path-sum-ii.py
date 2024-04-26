class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def twoMins(arr):
            min1 = float("inf")
            min2 = float("inf")
            
            for num in arr:
                if num<min1:
                    min2 = min1
                    min1 = num
                
                elif num<min2:
                    min2 = num
            
            return (min1,min2)
        
        for i in range(1,m):
            min1, min2 = twoMins(grid[i-1])  #1
			
            for j in range(n):
                minVal = min1
                if min1 == grid[i-1][j]:     #2
                    minVal = min2            #3
					
                grid[i][j] = grid[i][j] + minVal
        
        return min(grid[-1])