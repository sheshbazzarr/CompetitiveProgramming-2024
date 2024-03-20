class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[]
        for i in range(1,n+1,1):
            l.append(i)
        
        ind=0
        while len(l)>1:
            ind=(ind+k-1)%n
            l.pop(ind)
            n=n-1
        return l[0]