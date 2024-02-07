class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        len_i = len(nums)
        if len_i <= 1:
            return nums
        
        mid = len_i // 2
        nums1 = self.sortArray(nums[:mid])  # Corrected the reference to self.sortArray
        nums2 = self.sortArray(nums[mid:])  # Corrected the reference to self.sortArray
        
        return self.Merge(nums1, nums2)  # Corrected the reference to self.Merge
    
    def Merge(self, A, B):  # Added self parameter to Merge method
        newarray = []
        while A and B:  # Simplified condition
            if A[0] < B[0]:
                newarray.append(A.pop(0))  # Using pop() to remove and get the first element
            else:
                newarray.append(B.pop(0))  # Using pop() to remove and get the first element
        newarray.extend(A)  # Appending remaining elements in A
        newarray.extend(B)  # Appending remaining elements in B
        return newarray