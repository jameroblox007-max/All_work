def get_stats(arr):
    n = len(arr)
    max_val = arr[0]
    min_val = arr[0]
    total_sum = 0
    
    i = 0
    while i < n:
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
        total_sum += arr[i]
        i += 1
        
    avg_val = total_sum / n
    return max_val, min_val, avg_val

def get_max_min_index(arr):
    n = len(arr)
    max_val = arr[0]
    min_val = arr[0]
    max_idx = 0
    min_idx = 0
    
    i = 1
    while i < n:
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
        i += 1
        
    return max_idx, min_idx

def search_value(arr, target):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == target:
            return i
        i += 1
    return -1

def count_above_average(arr):
    n = len(arr)

    total_sum = 0
    i = 0
    while i < n:
        total_sum += arr[i]
        i += 1
    avg_val = total_sum / n

    count = 0
    j = 0
    while j < n:
        if arr[j] > avg_val:
            count += 1
        j += 1
        
    return count

def is_increasing(arr):
    n = len(arr)
    i = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            return False
        i += 1
    return True

n = int(input("จำนวนตัวเลข: "))
numbers = []

i = 0
while i < n:
    x = float(input(f"ใส่ค่าตัวที่ {i+1}: "))
    numbers.append(x)
    i += 1

increasing_status = is_increasing(numbers)
max_val, min_val, avg_val = get_stats(numbers)
max_idx, min_idx = get_max_min_index(numbers)
above_avg_count = count_above_average(numbers)

print(f"\n--- ผลสรุปสถิติ ---")
print(f"ข้อมูลดั้งเดิม: {numbers}")
print(f"ค่าสูงสุด: {max_val} (ตำแหน่ง index: {max_idx})")
print(f"ค่าต่ำสุด: {min_val} (ตำแหน่ง index: {min_idx})")
print(f"ค่าเฉลี่ย (Average): {avg_val:.2f}")
print(f"จำนวนข้อมูลที่มากกว่าค่าเฉลี่ย: {above_avg_count} ตัว")
print(f"ข้อมูลเรียงจากน้อยไปมากหรือไม่: {increasing_status}")

search_target = float(input("\nใส่ค่าที่ต้องการค้นหา: "))
found_idx = search_value(numbers, search_target)
if found_idx != -1:
    print(f"พบค่า {search_target} ที่ index: {found_idx}")
else:
    print(f"ไม่พบค่า {search_target} ในข้อมูล")