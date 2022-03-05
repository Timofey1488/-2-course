# исходные данные
C = [[0.01, 0, -0.02, 0, 0],
     [0.01, 0.01, -0.02, 0, 0],
     [0, 0.01, 0.01, 0, -0.02],
     [0, 0, 0.01, 0.01, 0],
     [0, 0, 0, 0.01, 0.01]]

D = [[1.33, 0.21, 0.17, 0.12, -0.13],
     [-0.13, -1.33, 0.11, 0.17, 0.12],
     [0.12, -0.13, -1.33, 0.11, 0.17],
     [0.17, 0.12, -0.13, -1.33, 0.11],
     [0.11, 0.67, 0.12, -0.13, -1.33]]

A = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

b = [1.2, 2.2, 4.0, 0, -1.2]
results = [0, 0, 0, 0, 0]
multiple = [0, 0, 0, 0, 0]
k = 9
tmp = 0

#  вычисление матрицы А
def func_matrix_a(A):
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            A[i][j] = k * C[i][j] + D[i][j]


#  вывод матрицы А
def func_print_matrix_a(A):
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            print("{:.2f}".format(A[i][j]), end=' ')
        print("|", "{:.2f}".format(b[i]))


def func_sol_simple_iter(A, S, results, b, multiple):
    for i in range(len(A)):
        tmp = 0 
        for j in range(len(A[i])):
            S += A[i][j] * multiple[tmp]
            tmp += 1
        S -= A[i][i] * multiple[i]
        results[i] = (b[i]- S) / (A[i][i])
        S = 0


def func_sol_zeidel(A, S, results, b, multiple):
    for i in range(len(A)):
        tmp = 0 
        for j in range(len(A[i])):
            S += A[i][j] * multiple[tmp]
            tmp += 1
        S -= A[i][i] * multiple[i]
        results[i] = (b[i]- S) / (A[i][i])
        S = 0


def main():
    S = 0
    ip = 0
    iz = 0
    func_matrix_a(A)
    print("Original Matrix:\n")
    func_print_matrix_a(A)

    #  проверяем условие на сходимость
    for i in range(len(A)):
        for j in range(i, len(A[i])):
            S += A[i][j]
        S -= A[i][i]
        if abs(A[i][i]) > abs(S):
            print("True")
        else:
            print("False")

    # итерации
    for i in range(1, k - 1):
        ip += 1
        func_sol_simple_iter(A, S, results, b, multiple)
        for j in range(len(A)):
            multiple[j] = results[j]
    print("\nThe Method of Simple Iterations:\nWe need ", ip, " iterations")
    for i in range(len(A)):
        print(f"x[{i}]=","{:.4f}".format(multiple[i]))

    S = 0
    for i in range(1, k - 3):
        iz += 1
        func_sol_zeidel(A, S, results, b, multiple)
        for j in range(len(A)):
            multiple[j] = results[j]
    print("\nThe Method of Zeidel:\nWe need ", iz, " iterations")
    for i in range(len(A)):
        print(f"x[{i}]=", "{:.4f}".format(multiple[i]))


if __name__ == "__main__":
    main()






