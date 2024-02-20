class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        max_consecutive = 0
        max_count = 0
        
        counts = {"T": 0, "F":0 }
        left = right = 0

        while right < n:
            counts[answerKey[right]] += 1
            max_count = max(max_count, counts[answerKey[right]])

            if (right - left + 1) - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1
            
            max_consecutive = max(max_consecutive, right - left + 1)
            right += 1

        return max_consecutive