class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        random_count=[100]*26
        for s in words:
            current_count=[0]*26
            for c in s:
                current_count[ord(c)-ord('a')]+=1
            for c in range(26):
                random_count[c]=min(random_count[c],current_count[c])
                
        result=[]
        for c in range(26):
            for _ in range(random_count[c]):
                result.append(chr(c+ord("a")))
        return result