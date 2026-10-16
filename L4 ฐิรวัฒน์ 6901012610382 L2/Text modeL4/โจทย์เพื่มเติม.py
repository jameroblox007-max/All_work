arr = [15, 8, 23, 42, 7, 19]
target = 1

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Found at index {i}")
        found = True
        break

if not found:
    print("Not found")