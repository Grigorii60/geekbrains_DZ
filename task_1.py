class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f"{' '.join(map(str, self.matrix[0]))}\n{' '.join(map(str, self.matrix[1]))} "\
               f"\n{' '.join(map(str, self.matrix[2]))}"

    def __add__(self, other):
        result = [[0, 0], [0, 0], [0, 0]]
        for i in range(len(self.matrix)):

            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] + other.matrix[i][j]
        for r in result:
            print(' '.join(map(str, r)))


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
matrix_1 + matrix_2
