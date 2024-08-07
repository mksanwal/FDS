class SparseMatrix:
    def __init__(self):
        self.matrix = {}

    def set_value(self, row, col, value):
        if value != 0:
            self.matrix[(row, col)] = value
        elif (row, col) in self.matrix:
            del self.matrix[(row, col)]

    def get_value(self, row, col):
        return self.matrix.get((row, col), 0)

    def transpose(self):
        transposed = SparseMatrix()
        for (row, col), value in self.matrix.items():
            transposed.set_value(col, row, value)
        return transposed

    def fast_transpose(self):

        rows = max(row for row, _ in self.matrix) + 1
        cols = max(col for _, col in self.matrix) + 1
        transposed = SparseMatrix()
        for (row, col), value in self.matrix.items():
            transposed.set_value(col, row, value)
        return transposed

    def add(self, other):
        result = SparseMatrix()
        all_keys = set(self.matrix.keys()).union(other.matrix.keys())
        for key in all_keys:
            value = self.get_value(*key) + other.get_value(*key)
            if value != 0:
                result.set_value(*key, value)
        return result

    def __str__(self):
        if not self.matrix:
            return "Empty Matrix"
        rows = [f"{row},{col}: {value}" for (row, col), value in self.matrix.items()]
        return "\n".join(rows)


if __name__ == "__main__":

    mat1 = SparseMatrix()
    mat2 = SparseMatrix()


    mat1.set_value(0, 1, 5)
    mat1.set_value(1, 2, 8)
    mat1.set_value(2, 3, 10)

   
    mat2.set_value(1, 0, 4)
    mat2.set_value(2, 1, 6)
    mat2.set_value(3, 2, 7)

 
    print("Matrix 1:")
    print(mat1)
    print("\nMatrix 2:")
    print(mat2)

   
    print("\nTranspose of Matrix 1:")
    print(mat1.transpose())

    print("\nFast Transpose of Matrix 1:")
    print(mat1.fast_transpose())

    
    print("\nSum of Matrix 1 and Matrix 2:")
    print(mat1.add(mat2))
