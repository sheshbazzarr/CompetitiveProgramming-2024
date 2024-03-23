class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        even_Index=[]
        odd_Index=[]
        for i in range(len(nums)):
            if i %2==0:
                even_Index.append(nums[i])
            else:
                odd_Index.append(nums[i])
        even_Index=sorted(even_Index)
        odd_Index=sorted(odd_Index,reverse=True)
        
        Sorted_Array=[0]*len(nums)
        
        for num in range(len(Sorted_Array)):
            if num %2==0:
                Sorted_Array[num]=even_Index[num//2]
            else:
                Sorted_Array[num]=odd_Index[num//2]
            
        return Sorted_Array
                
                
            