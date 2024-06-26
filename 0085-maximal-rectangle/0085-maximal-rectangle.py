class Solution:
    def histogram(self, heights):
        n = len(heights)
        st1 = deque()
        st2 = deque()
        left = [0] * n
        right = [0] * n

        # Previous smaller element
        for i in range(n):
            num = heights[i]

            while st1 and heights[st1[-1]] > num:
                st1.pop()

            if not st1:
                left[i] = -1
            else:
                left[i] = st1[-1]

            st1.append(i)

        # Next greater element
        for i in range(n - 1, -1, -1):
            num = heights[i]

            while st2 and heights[st2[-1]] >= num:
                st2.pop()

            if not st2:
                right[i] = n
            else:
                right[i] = st2[-1]

            st2.append(i)

        max_area = 0
        for i in range(n):
            area = (right[i] - left[i] - 1) * heights[i]
            max_area = max(max_area, area)

        return max_area

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        curr_row = [0] * len(matrix[0])
        max_area = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    curr_row[j] += 1
                else:
                    curr_row[j] = 0

            curr_max = self.histogram(curr_row)
            max_area = max(max_area, curr_max)

        return max_area