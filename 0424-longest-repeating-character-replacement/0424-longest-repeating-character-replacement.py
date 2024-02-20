class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0
        count = defaultdict(int)

        left = 0
        for right in range(n):
            count[s[right]] += 1
            max_count = max(count.values())

            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length