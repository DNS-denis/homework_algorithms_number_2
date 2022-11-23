# Сложность O(n)
# принимает значения целочисленного массива и возвращает максимальную прибыль
class Solution:
    def maxScoreSightseeingPair(self, values):
        max_profit = 0
        curr = 0
        for i in range(1, len(values)):
            curr = max(curr, values[i-1] + i-1)
            max_profit = max(max_profit, curr + values[i]-i)
        return max_profit