class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 128
        for char in s:
            ascii_value = ord(char)
            dp[ascii_value] = max(dp[ascii_value - k : ascii_value + k + 1]) + 1
        return max(dp)