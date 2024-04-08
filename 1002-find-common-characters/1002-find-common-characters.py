class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d=dict()
        res=[]
        for ele in words[0]:
            if ele not in d:
                d[ele]=[1]
            else:
                d[ele][0]+=1
        for i in range(1,len(words)):
            for ele in words[i]:
                if ele in d.keys():
                    if len(d[ele])==i:
                        d[ele].append(1)
                    else:
                        d[ele][-1]+=1
        for key in d.keys():
            if len(d[key])==len(words):
                temp=key*min(d[key])
                temp.split()
                res+=temp
        return res