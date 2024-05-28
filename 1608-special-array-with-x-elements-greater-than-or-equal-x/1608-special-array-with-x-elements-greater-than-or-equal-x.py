class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def count_greater_equal(arr, num):
            count = 0
            for element in arr:
                if element >= num:
                    count += 1
            return count

        nums.sort()
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            count = count_greater_equal(nums, mid)

            if count == mid:
                return mid
            elif count > mid:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        
            
        
        