class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        fractions=[]
        #generate all possible fractions
        for i in range(n):
            for j in range(i+1,n):
                fractions.append((arr[i],arr[j]))
        fractions.sort(key=lambda x:x[0]/x[1])
        return fractions[k-1]
        
        