# Сложность O(n+1)
# принимает длину списка и возвращает int: максимальный элемент в этом списке
class Solution:
    def getMaximumGenerated(self, n):
        if not n:
            return n
        numbers = [0] * (n+1)
        numbers[1] = 1
        for i in range(2, n+1):
            if i % 2:
                numbers[i] = numbers[i//2] + numbers[i//2+1]
            else:
                numbers[i] = numbers[i//2]
        return max(numbers)