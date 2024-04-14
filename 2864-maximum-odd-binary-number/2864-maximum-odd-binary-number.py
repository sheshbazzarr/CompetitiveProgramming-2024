class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        max_string=['0']*len(s)
        count_one=0
        for one in range(len(s)):
            if s[one]=="1":
                max_string[count_one]='1'
                count_one+=1
        max_string[count_one-1],max_string[-1]=max_string[-1],'1'
        return "".join(max_string)
                
        
   
                    