class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
      
        output=0
        hashmap={}
        for n in nums:
            if n in hashmap:
                output+=hashmap[n]
                hashmap[n]+=1
            else:
                hashmap[n]=1
        return output
                