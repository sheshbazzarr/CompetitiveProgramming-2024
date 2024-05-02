class Solution:
    def findMaxK(self, nums: List[int]) -> int:
         # [1] two use two-pointers approach, we need
        #     to prepare the list by sorting
        nums.sort()
        
        # [2] move pointers towards each other to find
        #     largest positive integer with its negative
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] == - nums[j]:
                return nums[j]
            if abs(nums[i]) > abs(nums[j]):
                i += 1
            else:
                j -= 1
                
        return -1