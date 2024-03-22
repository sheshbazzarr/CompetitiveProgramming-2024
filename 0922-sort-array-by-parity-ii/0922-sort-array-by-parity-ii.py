class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left_even, right_odd = 0, 1
        while left_even < len(nums) and right_odd < len(nums):
            if nums[left_even] % 2 == 0:
                left_even += 2
            elif nums[right_odd] % 2 == 1:
                right_odd += 2
            else:
                nums[left_even], nums[right_odd] = nums[right_odd], nums[left_even]
        return nums
