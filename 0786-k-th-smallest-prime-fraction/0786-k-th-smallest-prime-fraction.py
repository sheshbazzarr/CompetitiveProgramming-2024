class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        n = len(arr)
        
        # Generate all possible fractions
        for i in range(n):
            for j in range(i + 1, n):
                fractions.append((arr[i], arr[j]))
        
        # Sort fractions by value
        fractions.sort(key=lambda x: x[0] / x[1])
        
        # Return the kth smallest fraction
        return fractions[k - 1]