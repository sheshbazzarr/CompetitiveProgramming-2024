class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_color = image[sr][sc]
        height = len(image)
        width = len(image[0])

        def dfs(sr, sc):
            # Check if the current pixel is within the image bounds and has the same color as the starting pixel
            if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == cur_color and image[sr][sc] != color:
                # Update the color
                image[sr][sc] = color

                # Recursively call DFS for neighboring pixels
                dfs(sr + 1, sc)
                dfs(sr - 1, sc)
                dfs(sr, sc + 1)
                dfs(sr, sc - 1)

        dfs(sr, sc)
        return image

        dfs(sr,sc)
        return image