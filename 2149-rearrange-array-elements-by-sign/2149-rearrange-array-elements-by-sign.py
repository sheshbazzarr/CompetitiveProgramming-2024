class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        _reArray=[0]*(len(nums))
        pos_num,neg_num=0,1
        for num in nums:
            if num>0:
                _reArray[pos_num]=num
                pos_num+=2
            elif num<0:
                _reArray[neg_num]=num
                neg_num+=2
        return _reArray
                