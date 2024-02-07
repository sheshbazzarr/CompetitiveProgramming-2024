class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        len_i=len(nums)
        if len_i==1:
            return nums
        mid=int(len_i/2)
        nums1=self.sortArray(nums[0:mid])
        nums2=self.sortArray(nums[mid:])
        
        return self.Merge(nums1,nums2) 
    
    def Merge(self,A,B):
        newarray=[]
        while len(A)>0 and len(B)>0:
            if A[0]<B[0]:
                newarray.append(A[0])
                A.pop(0)
            else:
                newarray.append(B[0])
                B.pop(0)
        if len(A)==0:
            newarray+=B
        if len(B)==0:
            newarray+=A
        return newarray