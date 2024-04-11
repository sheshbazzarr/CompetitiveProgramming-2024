class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        s = sorted(arr)
        if arr == s:
            return []

        flips = []
        for pancake in range(n):
            m = arr.index(max(arr[:n-pancake]))
            if m != n-pancake-1:
                arr[:m+1] = arr[:m+1][::-1]
                arr[:n-pancake] = arr[:n-pancake][::-1]
                flips.extend([m+1, n-pancake])
        
        return flips