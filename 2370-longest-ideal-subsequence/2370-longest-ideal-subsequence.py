class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
      
        ideal_len=[0]*128
        for chr in s:
            asic_va=ord(chr)
            min_ed=asic_va-k
            max_ed=asic_va+k
            curr_len=max(ideal_len[min_ed:max_ed+1])+1
            ideal_len[asic_va]=curr_len
        return max(ideal_len)