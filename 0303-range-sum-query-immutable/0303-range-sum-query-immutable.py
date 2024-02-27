class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        

    def sumRange(self, left, right):
        summ = sum(self.nums[left:right+1])
        return summ


