student = {
    "id": "6901012610382",
    "name": "Thirawat",
    "age": 18,
    "major": "Computer Engineering"
}

print("Student information:")
print(student)

print("\nName:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])

student["year"] = 1

print("\nAfter adding year:")
print(student)

del student["year"]

print("\nAfter deleting year:")
print(student)

print("\nAll student information:")

for key, value in student.items():
    print(key, ":", value)