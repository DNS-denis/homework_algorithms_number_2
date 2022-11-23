# Сложность O(n*m)
# принимает матрицу, в которой мы ищем квадраты и возвращает количество квадратов в матрице
class Solution:
    def countSquares(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] > 0:
                    matrix[i][j] = 1 + min(matrix[i][j-1], matrix[i-1][j-1], matrix[i-1][j])
        q = 0
        for subj in matrix:
            q += sum(subj)
        return q