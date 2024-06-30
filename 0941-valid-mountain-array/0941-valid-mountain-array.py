class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        A=0
        B=len(arr)-1
        D=len(arr)
        while A+1<D and arr[A]<arr[A+1]:
            A+=1 
        while B>0 and arr[B]<arr[B-1]:
            B-=1
        return 0<A==B<D-1