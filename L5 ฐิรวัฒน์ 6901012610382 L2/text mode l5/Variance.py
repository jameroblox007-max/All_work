def calculate_variance(numbers):
    n = len(numbers)

    if n == 0:
        return 0.0

    total_sum = 0
    i = 0
    while i < n:
        total_sum += numbers[i]
        i += 1
    mean = total_sum / n

    sum_squared_diff = 0
    j = 0
    while j < n:
        diff = numbers[j] - mean
        sum_squared_diff += diff ** 2
        j += 1

    variance = sum_squared_diff / n
    return variance

data = [10, 12, 23, 23, 16, 23, 21, 16]
result = calculate_variance(data)

print(f"ข้อมูล: {data}")
print(f"ค่าความแปรปรวน (Variance): {result:.2f}")