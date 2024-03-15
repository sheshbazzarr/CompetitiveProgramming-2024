class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for i in range(len(plants)):
            if water >= plants[i]:
                water -= plants[i]
                steps += 1
            else:
                steps += (2*i) + 1
                water = capacity
                water -= plants[i]
        return steps