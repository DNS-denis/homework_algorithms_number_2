# Сложность O((n+1)*(m+1))
# принимает сетку, которую мы должны исследовать +
# возвращает количество возможных уникальных путей, по которым робот может пройти, чтобы добраться до нижнего правого угла
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0][1] = 1

        for row in range(1, m+1):
            for col in range(1, n+1):
                if not obstacleGrid[row-1][col-1]:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]
        print(dp)
        return dp[-1][-1]