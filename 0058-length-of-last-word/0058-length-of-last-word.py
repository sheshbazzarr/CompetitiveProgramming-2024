class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        note=s.split()
        last=note[-1]
        return len(last)