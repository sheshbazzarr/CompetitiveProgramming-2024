class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
       
        N=len(score)
        score_with_index=list((score,index) for index,score in enumerate(score))
        score_with_index.sort(reverse=True)
        ans=[0]*N
        for rank,(score,index) in enumerate(score_with_index):
            match rank:
                case 0:
                    ans[index]="Gold Medal"
                case 1:
                    ans[index]="Silver Medal"
                case 2:
                    ans[index]="Bronze Medal"
                case x:
                    ans[index]=str(rank+1)
        return ans