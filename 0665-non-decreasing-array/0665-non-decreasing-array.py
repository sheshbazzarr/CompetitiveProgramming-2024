class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for num in range(1, len(nums)):
            if nums[num] < nums[num-1]:
                if num > 1 and nums[num-2] > nums[num]:
                    nums[num] = nums[num-1]
                count += 1
        return count <= 1
                    
                