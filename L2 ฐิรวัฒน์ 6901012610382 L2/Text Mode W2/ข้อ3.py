n = int(input("จำนวนตัวเลข: "))
numbers = []

for i in range(n):
    x = float(input(f"ใส่ค่าตัวที่ {i+1}: "))
    numbers.append(x)

for i in range(n):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print("ค่ามัธยฐานคือ:", median)