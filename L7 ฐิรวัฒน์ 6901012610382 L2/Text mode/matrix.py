my_array = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]


def analyze_array(arr):
    max_val = arr[0][0]
    min_val = arr[0][0]
    total_sum = 0
    count = 0
    
    for row in arr:
        for val in row:
            if val > max_val:
                max_val = val
            if val < min_val:
                min_val = val
            total_sum += val
            count += 1
            
    average = total_sum / count if count > 0 else 0
    return max_val, min_val, average

def is_found(arr, target):
    for row in arr:
        if target in row:
            return True
    return False

def matrix_add(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 * cols for _ in range(cols)] for _ in range(rows)] 
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    return result

def matrix_subtract(A, B):
    rows = len(A)
    cols = len(A[0])
    result = [[0 * cols for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] - B[i][j]
    return result

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        return "Matrix dimensions do not match for multiplication"
        
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

print("ข้อ a")
mx, mn, avg = analyze_array(my_array)
print(f"Max: {mx}, Min: {mn}, Average: {avg}")

print("\nข้อ b")
print("Is 50 found?", is_found(my_array, 50))
print("Is 99 found?", is_found(my_array, 99))

print("\nข้อ c")
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("Matrix Addition:", matrix_add(A, B))
print("Matrix Subtraction:", matrix_subtract(B, A))
print("Matrix Multiplication:", matrix_multiply(A, B))