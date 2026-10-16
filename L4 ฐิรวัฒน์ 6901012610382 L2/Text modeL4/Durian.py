count = 0
total = 0

weight = int(input("Please input Durian weight: "))
while weight != 0:
    count += 1
    total += weight
    weight = int(input("Please input Durian weight: "))

print()
print("Total of", count, "Durians")
print("Average weight is", total / count)