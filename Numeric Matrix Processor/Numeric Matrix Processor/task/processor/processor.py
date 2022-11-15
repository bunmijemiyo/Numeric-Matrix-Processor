import numpy as np


def menu_screen():
    print("\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix"
          "\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")


def add_matrix():
    row, col = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix: ")
    matrix = [[float(x) for x in input().split()] for _ in range(row)]
    row2, col2 = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix: ")
    matrix2 = [[float(x) for x in input().split()] for _ in range(row2)]
    mat = []
    if row == row2 and col == col2:
        for i in range(row):
            mat.append([])
            for j in range(col2):
                mat[i].append(0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat[i][j] += matrix[i][j] + matrix2[i][j]
        print("The result is: ")
        for s in mat:
            print(*s)
    else:
        print("The operation cannot be performed.")


def multiply_matrix_with_constant():
    row, col = map(int, input("Enter size of matrix: ").split())
    print("Enter matrix: ")
    matrix = [[float(x) for x in input().split()] for _ in range(row)]
    constant = float(input("Enter constant: "))
    mat = []
    for i in range(row):
        mat.append([])
        for j in range(col):
            mat[i].append(0)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            mat[i][j] += constant * matrix[i][j]
    print("The result is: ")
    for s in mat:
        print(*s)


def multiply_two_matrix():
    row, col = map(int, input("Enter size of first matrix: ").split())
    print("Enter first matrix: ")
    matrix = [[float(x) for x in input().split()] for _ in range(row)]
    row2, col2 = map(int, input("Enter size of second matrix: ").split())
    print("Enter second matrix: ")
    matrix2 = [[float(x) for x in input().split()] for _ in range(row2)]
    mat = []
    if col == row2:
        for i in range(row):
            mat.append([])
            for j in range(col2):
                mat[i].append(0)
        for i in range(len(matrix)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    mat[i][j] += matrix[i][k] * matrix2[k][j]
        print("The result is: ")
        for s in mat:
            print(*s)
    else:
        print("The operation cannot be performed.")


def transpose_options():
    print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice2 = input("Your choice: ")
    row, col = map(int, input("Enter matrix size: ").split())
    print("Enter matrix: ")
    matrix = [[float(x) for x in input().split()] for _ in range(row)]
    if choice2 == "1":
        mat = []
        for i in range(row):
            mat.append([])
            for j in range(col):
                mat[i].append(0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mat[i][j] = matrix[j][i]
        print("The result is: ")
        for s in mat:
            print(*s)
    elif choice2 == "2":
        transpose_list = [elem[::-1] for elem in matrix]
        mat = []
        for i in range(row):
            mat.append([])
            for j in range(col):
                mat[i].append(0)
        for i in range(len(transpose_list)):
            for j in range(len(transpose_list[0])):
                mat[i][j] = transpose_list[j][i]
        transpose_list2 = [elem[::-1] for elem in mat]
        print("The result is: ")
        for s in transpose_list2:
            print(*s)
    elif choice2 == "3":
        transpose_list4 = [elem[::-1] for elem in matrix]
        print("The result is: ")
        for s in transpose_list4:
            print(*s)
    elif choice2 == "4":
        transpose_list3 = [elem[::-1] for elem in matrix][::-1]
        print("The result is: ")
        for s in transpose_list3:
            print(*s[::-1])


def matrix_determinant(matrix, total=0):
    indices = list(range(len(matrix)))
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2 and len(matrix[0]) == 2:
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val

    for fc in indices:
        new_matrix = matrix
        new_matrix = new_matrix[1:]
        height = len(new_matrix)

        for i in range(height):
            new_matrix[i] = new_matrix[i][0:fc] + new_matrix[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = matrix_determinant(new_matrix)
        total += matrix[0][fc] * sign * sub_det

    return total


while True:
    menu_screen()
    choice = input("Your choice: ")
    if choice == "0":
        break
    elif choice == "1":
        add_matrix()
    elif choice == "2":
        multiply_matrix_with_constant()
    elif choice == "3":
        multiply_two_matrix()
    elif choice == "4":
        transpose_options()
    elif choice == "5":
        row, col = map(int, input("Enter matrix size: ").split())
        print("Enter matrix: ")
        matrix = [[int(i) if i.isdigit() else float(i) for i in input().split()] for i in range(row)]
        if row != col:
            print("The operation cannot be performed.")
        else:
            print("The result is: ")
            print(matrix_determinant(matrix, total=0))
    elif choice == "6":
        row, col = map(int, input("Enter matrix size: ").split())
        print("Enter matrix: ")
        matrix = [[int(i) if i.isdigit() else float(i) for i in input().split()] for i in range(row)]
        if row != col:
            print("The operation cannot be performed.")

        else:
            if matrix_determinant(matrix, total=0) == 0:
                print("This matrix doesn't have an inverse.")
            else:
                print("The result is: ")
                matrix_inverse = np.linalg.inv(matrix)
                for inverse in matrix_inverse:
                    print(*inverse)