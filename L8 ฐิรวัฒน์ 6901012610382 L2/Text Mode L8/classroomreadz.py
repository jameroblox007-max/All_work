import csv

class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = age

    def show(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Course: {self.course} | Age: {self.age}")


def read_students(filename):
    students = []
    with open(filename, encoding="utf-8") as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)  # skip header
        for row in reader:
            students.append(Student(row[0], row[1], row[2], int(row[3])))
    return students


def show_youngest(students):
    min_age = min(s.age for s in students)
    for s in students:
        if s.age == min_age:
            s.show()


students = read_students("classroomz.txt")
show_youngest(students)