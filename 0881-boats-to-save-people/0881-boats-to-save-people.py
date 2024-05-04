from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right_p = len(people) - 1
        count = 0
        while left <= right_p:
            if people[left] + people[right_p] <= limit:
                left += 1
                right_p -= 1
            else:
                right_p -= 1
            count += 1
        return count
