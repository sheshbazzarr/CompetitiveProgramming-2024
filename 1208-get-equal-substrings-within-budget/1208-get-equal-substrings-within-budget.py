class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]

        # Create prefix sum array
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + cost[i]

        def canMakeSubstring(length):
            for i in range(n - length + 1):
                totalCost = prefix_sum[i + length] - prefix_sum[i]
                if totalCost <= maxCost:
                    return True
            return False

        # Binary search for maximum length
        left, right = 0, n
        while left < right:
            mid = (left + right + 1) // 2
            if canMakeSubstring(mid):
                left = mid
            else:
                right = mid - 1

        return left