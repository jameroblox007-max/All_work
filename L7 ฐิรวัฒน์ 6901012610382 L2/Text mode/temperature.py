temp = [
    [33, 34, 34, 34, 34, 33, 33], 
    [34, 32, 32, 33, 34, 33, 34], 
    [35, 34, 35, 35, 32, 32, 32], 
    [32, 32, 34, 34, 34, 34, 33],
]


def sort_list(arr):
    data = arr.copy() 
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

def weektemp_avr(temp_matrix, week):
    week_data = temp_matrix[week]
    return sum(week_data) / len(week_data)


def week_max(temp_matrix, week):
    sorted_data = sort_list(temp_matrix[week])
    return sorted_data[-1]


def week_min(temp_matrix, week):
    sorted_data = sort_list(temp_matrix[week])
    return sorted_data[0]


n = int(input("สัปดาห์ (1-4) = "))
w = n - 1  


avg_result = weektemp_avr(temp, w)
max_result = week_max(temp, w)
min_result = week_min(temp, w)


print(f"ค่าเฉลี่ยอุณหภูมิสัปดาห์ที่ {w+1} คือ: {avg_result:.2f} °C")
print(f"อุณหภูมิมากที่สุด = {max_result} °C")
print(f"อุณหภูมิต่ำสุด = {min_result} °C")