class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        newarray=[]
        for i in range(1,n+1,1):
            newarray.append(i)
        countstartindex=0
        while len(newarray)>1:
            countstartindex=(countstartindex+k-1)%n
            newarray.pop(countstartindex)
            n=n-1
        return newarray[0]