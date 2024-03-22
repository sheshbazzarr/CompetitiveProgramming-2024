class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
#         this is not effective solution thou
        positive = deque()
        negative = deque()
        result = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        while positive or negative:
            if positive:
                result.append(positive.popleft())
            if negative:
                result.append(negative.popleft())

            if not positive:
                result.extend(negative)
                break
            if not negative:
                result.extend(positive)
                break

        return result