class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#         this is not effective solution thou
        post=[]
        negat=[]
        result=[]
        for num in nums:
            if num>0:
                post.append(num)
            else:
                negat.append(num)
        for i in range(len(post)):
            result.append(post[i])
            result.append(negat[i])
        return result