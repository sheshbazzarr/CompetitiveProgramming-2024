class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ideal_lengths = [0] * 128
        for char in s:
            ascii_value = ord(char)
            current_ideal_length = max(ideal_lengths[ascii_value - k : ascii_value + k + 1]) + 1
            ideal_lengths[ascii_value] = current_ideal_length
        max_ideal_length = max(ideal_lengths)
        return max_ideal_length