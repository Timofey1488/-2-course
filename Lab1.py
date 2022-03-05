import numpy


#Все исходные данные
C= [[0.2, .0, 0.2, .0, 0.2],
     [.0, 0.2, .0, 0.2, .0],
     [0.2, .0, 0.2, .0, 0.2],
     [.0, 0.2, .0, 0.2, .0],
     [.0, .0, 0.2, .0, 0.2]]

D = [[2.33, 0.81, 0.67, 0.92, -0.53],
     [-0.53, 2.33, 0.81, 0.67, 0.92],
     [0.92, -0.53, 2.33, 0.81, 0.67],
     [0.67, 0.92, -0.53, 2.33, 0.81],
     [0.81, 0.67, 0.92, -0.53, 2.33]]

A = [[0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0]]

b = [4.2, 4.2, 4.2, 4.2, 4.2]
results = [0,0,0,0,0]
k = 9
tmp = 0
S = 0

#вычисление матрицы А
def func_matrixA(A):
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            A[i][j] = k * C[i][j] + D[i][j]
func_matrixA(A)       
        
print("Исходная матрица:\n");

#вывод матрицы А
def func_print_matrixA(A):
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            print("{:.4f}".format(A[i][j]), end=' ')
        print()
func_print_matrixA(A)

#приведение матрицы к треугольному виду
def func_triangle_view(A):
    for i in range(len(A)): 
        for j in range(i+1,len(A[i])):
            tmp = A[j][i] / A[i][i]
            b[j] -= tmp * b[i]
            A[j][i] = 0
            for l in range(i+1,len(A[i])):
                A[j][l] -= tmp * A[i][l]
func_triangle_view(A)

#вывод матрицы А
print("\nПреобразованная матрица:\n");
def func_print_matrixA_triangle(A):
    for i in range(len(A)): 
        for j in range(len(A[i])):
            print("{:.4f}".format(A[i][j]),end=' ')
        print("|","{:.4f}".format(b[i]))
func_print_matrixA_triangle(A)
    
#ищем решения системы
for i in range(len(A)-1,-1,-1):
    for j in range(i,len(A[i])):
        if(j==len(A[i])-1):
            break
        else:
            b[i] -= A[i][j + 1] * results[j + 1]
    results[i] = b[i] / A[i][i]

print("\nРешения системы:\n")

#вывод решений
for i in range(len(A)):
    print("{:.10f}".format(results[i]))
#------------------------------------------    

#вычисление матрицы А
func_matrixA(A)   
#сброс b[i]
for i in range(len(A)):
    b[i] = 4.2
    
print("\nМетод Гаусса с выбором главного элемента по столбцу")
for i in range(len(A)):
    max_index = i
    max_ = A[i][i]
    for j in range(i+1,len(A[i])):
        if(abs(max_)<abs(A[j][i])):
            max_index = j
            max_ = A[j][i]
#перестанвока строк местами
    if(i != max_index):
        temp_root = b[i]
        b[i] = b[max_index]
        b[max_index] = temp_root
        for j in range(len(A[i])):
            temp = A[i][j]
            A[i][j] = A[max_index][j]
            A[max_index][j] = temp
            
#приведение матрицы к треугольному виду          
func_triangle_view(A)

print("\nПреобразованная матрица:\n");
#вывод матрицы A
func_print_matrixA_triangle(A)

#ищем решения системы
for i in range(len(A)-1,-1,-1):
    for j in range(i,len(A[i])):
        if(j==len(A[i])-1):
            break
        else:
            b[i] -= A[i][j + 1] * results[j + 1]
    results[i] = b[i] / A[i][i]

print("\nРешения системы:")

#вывод решений
for i in range(len(A)):
    print("{:.4f}".format(results[i]))
#-------------------------------------------
#вычисление матрицы А
func_matrixA(A)   
#сброс b[i]
for i in range(len(A)):
    b[i] = 4.2

print("\nМетод Гаусса с выбором главного элемента по всей матрице")
for i in range(len(A)):
    max_index = i
    max_ = A[i][i]
    for j in range(i,len(A[i])):
        for l in range(i,len(A[i])):
            if(abs(max_)<abs(A[j][l])):
                max_index = j
                max_ = A[j][l]
      
#перестановка строк местами
        if(i != max_index):
            temp_root = b[i]
            b[i] = b[max_index]
            b[max_index] = temp_root
            for j in range(len(A[i])):
                temp = A[i][j]
                A[i][j] = A[max_index][j]
                A[max_index][j] = temp
#приведение матрицы к треугольному виду          
func_triangle_view(A)
      
print("\nПреобразованная матрица:\n");
#вывод матрицы A
func_print_matrixA_triangle(A)

#ищем решения системы
for i in range(len(A)-1,-1,-1):
    for j in range(i,len(A[i])):
        if(j==len(A[i])-1):
            break
        else:
            b[i] -= A[i][j + 1] * results[j + 1]
    results[i] = b[i] / A[i][i]

print("\nРешения системы:")

#вывод решений
for i in range(len(A)):
    print("{:.4f}".format(results[i]))

#оценка
def occurancy(A, b, results):
    for i in range(len(results)):
        results[i] = results[i].__round__(4)
    vector_1 = numpy.linalg.solve(A, b)
    print(vector_1)
    print("\nАбсолютные погрешности:")
    for i in range(len(results)):
        print(f"\u039bx{i + 1} = |x-x{i + 1}|={results[i]} - {vector_1[i]} = {abs(vector_1[i] - results[i])}")
    print("\nОтносительные погрешности:")
    for i in range(len(results)):
        print(f"\u03b4{i + 1} = |x-x{i + 1}|/|x{i + 1}|=({results[i]} - {vector_1[i]})/{results[i]} = {abs(vector_1[i] - results[i]) / results[i]}")

occurancy(A, b, results)