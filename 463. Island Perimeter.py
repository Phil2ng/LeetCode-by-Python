class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # import scipy
        # print(sum(sum(scipy.array(grid))))

        # res = 4 * sum(map(sum, grid))
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res += 4
                    if i + 1 < len(grid) and grid[i + 1][j] == 1:
                        res -= 2
                    if j + 1 < len(grid[i]) and grid[i][j + 1] == 1:
                        res -= 2
        return res
