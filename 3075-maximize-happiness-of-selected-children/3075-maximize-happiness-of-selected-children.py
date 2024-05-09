class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness.sort()
        ans = 0
        n = len(happiness) - 1
        c = 0
        while n >= 0 and k > 0:
            if happiness[n] - c >= 0:
                ans += happiness[n] - c
            else:
                break
            c += 1
            n -= 1
            k -= 1
        return ans
