class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        _SortArr=[0]*len(nums)
        even_num,odd_num=0,1
        for num in nums:
            if num %2==0:
                _SortArr[even_num]=num
                even_num+=2
            elif num %2 !=0:
                _SortArr[odd_num]=num
                odd_num+=2
        return _SortArr