class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        prefix_sum = [0] * (n + 1)
        for firsti, lasti, seatsi in bookings:
            prefix_sum[firsti] += seatsi
            if lasti + 1 <= n:
                prefix_sum[lasti + 1] -= seatsi

        answer = [0] * n
        running_sum = 0
        for i in range(n):
            running_sum += prefix_sum[i + 1]
            answer[i] = running_sum

        return answer