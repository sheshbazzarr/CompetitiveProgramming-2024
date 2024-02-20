class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        num_zero=1
        left=0
        for right in range(len(nums)):
            num_zero-=nums[right]==0
            if num_zero<0:
                num_zero +=nums[left]==0
                left+=1
        return right-left