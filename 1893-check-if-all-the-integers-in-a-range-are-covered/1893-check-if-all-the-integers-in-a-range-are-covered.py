class Solution:
    def isCovered(self, ranges, left: int, right: int):
        covered = set()
        for i, j in ranges:
            for k in range(i, j + 1):
                covered.add(k)
        
        for i in range(left, right+1):
            if i not in covered:
                return False
        
        return True


# inputs = input().split()  # This splits the input string into a list of strings
# print(inputs)
        