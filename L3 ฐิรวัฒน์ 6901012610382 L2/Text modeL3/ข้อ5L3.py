n = int(input("จำนวนตัวเลข: "))
numbers = []

for i in range(n):
    x = float(input(f"ใส่ค่าตัวที่ {i+1}: "))
    numbers.append(x)

for i in range(n):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

mean = sum(numbers) / n

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

data_range = numbers[-1] - numbers[0]

print(f"\n--- ผลสรุปสถิติ ---")
print(f"ข้อมูลเรียงจากน้อยไปมาก: {numbers}")
print(f"ค่าเฉลี่ย (Mean): {mean:.2f}")
print(f"ค่ามัธยฐาน (Median): {median}")
print(f"ค่าพิสัย (Range): {data_range:.2f}")
