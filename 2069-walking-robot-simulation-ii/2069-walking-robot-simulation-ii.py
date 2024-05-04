from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.index = 0
        self.positions = [[0, 0, 'South']] + \
                        [[i, 0, 'East'] for i in range(1, width)] + \
                        [[width - 1, i, 'North'] for i in range(1, height)] + \
                        [[i, height - 1, 'West'] for i in range(width - 2, -1, -1)] + \
                        [[0, i, 'South'] for i in range(height - 2, 0, -1)]

    def step(self, num: int) -> None:
        self.index += num

    def getPos(self) -> List[int]:
        return self.positions[self.index % len(self.positions)][:2]

    def getDir(self) -> str:
        return self.positions[self.index % len(self.positions)][2] if self.index else 'East'

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
