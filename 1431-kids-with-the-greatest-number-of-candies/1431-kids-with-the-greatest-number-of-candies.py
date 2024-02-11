class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandi=max(candies)
        
        return [(curcandi+extraCandies>=maxcandi) for curcandi in candies]