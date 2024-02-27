class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_count = {0: 1} 

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            # Check if the complement of current remainder exists in the hashmap
            count += remainder_count.get(remainder, 0)

            # Update the hashmap with the current remainder
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return count