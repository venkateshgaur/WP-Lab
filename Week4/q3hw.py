class MatrixMultiplication:
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def multiply(self):
        rows_a = len(self.matrix_a)
        cols_a = len(self.matrix_a[0])
        rows_b = len(self.matrix_b)
        cols_b = len(self.matrix_b[0])
        
        if cols_a != rows_b:
            print("Matrix A's columns must equal Matrix B's rows for multiplication.")
            return None
        
        result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    result[i][j] += self.matrix_a[i][k] * self.matrix_b[k][j]
        
        return result

matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

multiplication = MatrixMultiplication(matrix_a, matrix_b)
result_matrix = multiplication.multiply()

if result_matrix:
    print("Resultant Matrix:")
    for row in result_matrix:
        print(row)