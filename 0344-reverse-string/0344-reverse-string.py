class Solution:
    def reverseString(self, s: List[str]) -> None:
        right = len(s) - 1
        left = 0
        while right > left:
            # Swap characters at indices left and right
            s[left], s[right] = s[right], s[left]
            right -= 1 
            left += 1