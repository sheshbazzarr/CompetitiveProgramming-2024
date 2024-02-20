class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hasho = {}
        most_frequent = 0
        start = 0
        max_len = 0

        for end, char in enumerate(s):
            hasho[char] = hasho.get(char, 0) + 1

            most_frequent = max(most_frequent, hasho[char])
            # (end - start + 1) --> window size
            if (end - start + 1) - most_frequent > k:
                hasho[s[start]] -= 1
                start += 1

            max_len = max(max_len, end-start+1)

        return max_len