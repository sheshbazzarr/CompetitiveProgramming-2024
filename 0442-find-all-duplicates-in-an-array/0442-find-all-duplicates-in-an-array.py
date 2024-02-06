class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output=[]
        for n in nums:
            m=abs(n)
            x=nums[m-1]
            if x<0:
                output.append(m)
            else:
                nums[m-1]*=-1
        return output