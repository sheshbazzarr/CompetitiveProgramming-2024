class Solution:
    def coloredCells(self, n: int) -> int:
        if n ==1:
            return 1
        else:
           return  self.coloredCells(n-1)+ 4*(n-1)