class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        idel_leng=[0]*128
        for chr in s:
            order_chr=ord(chr)
            adje_max=order_chr+k
            adje_min=order_chr-k
            test_adj=max(idel_leng[adje_min:adje_max+1])+1
            idel_leng[order_chr]=test_adj
        return max(idel_leng)
        