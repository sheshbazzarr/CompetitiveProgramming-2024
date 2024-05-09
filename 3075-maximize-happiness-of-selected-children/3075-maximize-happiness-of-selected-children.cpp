class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(),happiness.end());
        long long ans=0;
        int n=happiness.size()-1;
        int c=0;
        while (n>=0 && k>0){
            if(happiness[n]-c>=0)
                ans=ans+happiness[n]-c;
            else
                break;
            c++;
            n--;
            k--;
            
        }
        return ans;
        
    }
};