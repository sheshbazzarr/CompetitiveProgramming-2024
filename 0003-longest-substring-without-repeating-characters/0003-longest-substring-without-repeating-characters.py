class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = []
        substring = []

        for i in range(len(s)):
            cur_char = s[i]

            if cur_char not in substring:
                substring.append(cur_char)
                if len(substring) > len(longest):
                    longest = substring

            else:
                cut_idx = substring.index(cur_char)
                substring = substring[cut_idx+1:]
                substring.append(cur_char)

        return len(longest)