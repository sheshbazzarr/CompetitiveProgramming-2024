class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        c=[]
        for i in nums:
            if i >0:
                a.append(i)
            else:
                b.append(i)
        i,j=0,0
        while i<len(a) and j<len(b):
            c.append(a[i])
            i+=1
            c.append(b[j])
            j+=1
        return c
            
        