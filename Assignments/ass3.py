def add_matrices(n, m):
        result = []


        for i in range(len(n)):
            row = []
            for j in range(len(n[0])):
                row.append(n[i][j] + m[i][j])
            result.append(row)

        return result

def subtract_matrices(n, m):
    
        result = []

        for i in range(len(n)):
            row = []
            for j in range(len(n[0])):
                row.append(n[i][j] - m[i][j])
            result.append(row)

        return result


def multiply_matrices(n, m): 
        result = []

    
        for i in range(len(n)):
            row = []
            for j in range(len(m[0])):
                sum = 0
                for k in range(len(m)):
                    sum += n[i][k] * m[k][j]
                row.append(sum)
            result.append(row)

        return result

def diagonal_sum(matrix):

        n = len(matrix)
        main_sum = sum(matrix[i][i] for i in range(n))
        secondary_sum = sum(matrix[i][n - 1 - i] for i in range(n))

        return main_sum, secondary_sum

def upper_triangular(matrix):
     n = len(matrix)
     for i in range(n):
        row = []
        for j in range(n):
            if(matrix[i][j] != 0 and j>i):
                 return False

        return True


def saddle_point(matrix):
    n = len(matrix)
    for i in range (n):
        z=matrix[i]
        Min_matrix = min(z)
        y=z.index(Min_matrix)
        largest=Min_matrix
        for j in range(n):
            
            if(Min_matrix<matrix[j][y]):
                largest=matrix[j][y]
            
        if (largest==Min_matrix):
             print("Saddle point")
        else:
             continue

        

def input_matrix(prompt):

        rows = int(input("Number of rows: "))
        cols = int(input("Number of columns: "))

        
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input("Enter element at position ({i},{j}): "))
                row.append(element)
            matrix.append(row)

        return matrix


print("Enter Matrix 1-->>")
matrix1 = input_matrix("Matrix 1")

print("\nEnter Matrix 2-->>")
matrix2 = input_matrix("Matrix 2")


operation = input("\nEnter the operation to perform (1:addition/ 2:subtraction/ 3:multiplication/ 4:diagonal/ 5:upper_triangular/ 6:saddle_point").strip().lower()


if operation == "1":
        result = add_matrices(matrix1, matrix2)

        if result:
            print("\nResult of Addition:")
            for row in result:
                print(row)

elif operation == "2":
        result = subtract_matrices(matrix1, matrix2)

        if result:
            print("\nResult of Subtraction:")
            for row in result:
                print(row)

elif operation == "3":
        result = multiply_matrices(matrix1, matrix2)

        if result:
            print("\nResult of Multiplication:")
            for row in result:
                print(row)

elif operation == "4" :
    main_diag_sum, secondary_diag_sum = print(diagonal_sum(matrix1)) 

elif operation =="5":
    print (upper_triangular(matrix1))

elif operation == "6":
    print(saddle_point(matrix1))  
  
else:
    print("Invalid operation!!!   Please enter '1', '2', '3' , '4' ,'5' or '6'")

