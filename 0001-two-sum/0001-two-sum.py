class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            match = target - num
            if match in hashmap:
                return [hashmap[match], i]
            else:
                hashmap[num] = i
        return []