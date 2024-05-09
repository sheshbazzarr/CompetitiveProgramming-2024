class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort()
        n=len(happiness)-1
        c=0
        ans=0
        while k>0 and n>=0:
            if happiness[n]-c>0:
                ans+=happiness[n]-c
            else:
                break
            k-=1
            c+=1
            n-=1
                
        return ans
