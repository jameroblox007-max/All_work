arr = [3, 8, 12, 17, 25, 31, 42]

target = int(input("Enter number to search: "))

left = 0
right = len(arr) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(f"Found at index {mid}")
        found = True
        break

    elif target > arr[mid]:
        left = mid + 1

    else:
        right = mid - 1

if not found:
    print("Not found")