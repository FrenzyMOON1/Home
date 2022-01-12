class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda a: ' '.join(map(str, a)), self.matrix))

    def __add__(self, other):
        return Matrix(map(lambda a1, a2: map(lambda x, y: x + y, a1, a2), self.matrix, other.matrix))


mat1 = Matrix([[1, 2, 3], [4, 5, 6]])
mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
mat = mat1 + mat2
print(mat)