arr = [1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = int(input("Enter target: "))

left = 0
right = len(arr) - 1

found = False

while left < right:

    total = arr[left] + arr[right]

    if total == target:
        print(f"Found: {arr[left]} + {arr[right]} = {target}")
        found = True
        break

    elif total < target:
        left += 1

    else:
        right -= 1

if not found:
    print("Not found")