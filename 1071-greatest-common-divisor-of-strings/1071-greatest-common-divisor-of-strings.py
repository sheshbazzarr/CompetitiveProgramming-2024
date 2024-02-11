class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)<=len(str2):
            temp = str1
        else:
            temp = str2
        m = len(temp)
        x = 1
        res=[""]
        while x<=m:
            if m%x==0 and temp[:x] * (len(str1)//x) == str1 and temp[:x] * (len(str2)//x) == str2:
                res.append(temp[:x])
            x+=1
        return res[-1]