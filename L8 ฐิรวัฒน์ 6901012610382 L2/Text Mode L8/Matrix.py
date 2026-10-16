class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def show(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self.data[i][j], end=" ")
            print() 

    def add(self, other):

        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                sum_val = self.data[i][j] + other.data[i][j]
                row.append(sum_val)
            result.append(row)
        return Matrix(result)

    def subtract(self, other):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                sub_val = self.data[i][j] - other.data[i][j]
                row.append(sub_val)
            result.append(row)
        return Matrix(result)

    def multiplication(self, other):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                row.append(total)
            result.append(row)
        return Matrix(result)

A = Matrix([
    [1, 2],
    [3, 4]
])

B = Matrix([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
A.show()

print("\nMatrix B:")
B.show()

print("\nMatrix A + B:")
C = A.add(B)
C.show()

print("\nMatrix A - B:")
D = A.subtract(B)
D.show()

print("\nMatrix A * B:")
E = A.multiplication(B)
E.show()