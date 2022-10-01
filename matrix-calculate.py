import numpy as np

def createMatrix(row, column):
    matrix = []
    print("enter every parameter row by row, separated by space")
    for c in range(column):
        print("the", c+1, "line")
        subMartix = input()
        matrix.append(subMartix.split()[:row])
    print(matrix)
    return matrix


print("creating the first matrix(n)")
print("enter the row of the matrix(n)")
nr = int(input())
print("enter the column of the matrix(n)")
nc = int(input())

matrixN = createMatrix(nr, nc)

print("creating the first matrix(m)")
print("enter the row of the matrix(m)")
mr = int(input())
print("enter the column of the matrix(m)")
mc = int(input())

matrixM = createMatrix(mr, mc)

print("matrixN:", matrixN, "matrixM:", matrixM)

print(np.determinant(matrixN, matrixM))
