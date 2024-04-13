class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        LP=0
        RP=len(numbers)-1
        
        while RP>LP:
            if numbers[LP]+numbers[RP]==target:
                return [LP+1,RP+1]
            elif numbers[LP]+numbers[RP]>target:
                RP-=1
            else:
                LP+=1