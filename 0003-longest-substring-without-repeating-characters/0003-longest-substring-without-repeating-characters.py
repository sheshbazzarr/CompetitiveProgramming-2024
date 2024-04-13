class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=[]
        substring=[]
        
        for i in range(len(s)):
            chr_at_hand=s[i]
            
            if chr_at_hand not in substring:
                substring.append(chr_at_hand)
                if len(longest)<len(substring):
                    longest=substring
            else:
                find_dam_index=substring.index(chr_at_hand)
                substring=substring[find_dam_index+1:]
                substring.append(chr_at_hand)
        return len(longest)