class Person:
    def __init__(self, name, address, weight, height):
        self.name = name
        self.address = address
        self.weight = weight
        self.height = height

    def show(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Weight:", self.weight)
        print("Height:", self.height)

    def getBMI(self):
        return self.weight / (self.height ** 2)


class Student(Person):
    def __init__(self, name, address, weight, height, student_id, course, gpa):
        super().__init__(name, address, weight, height)
        self.student_id = student_id
        self.course = course
        self.gpa = gpa

    def show(self):
        super().show()
        print("BMI:", round(super().getBMI(), 2))
        print("Student ID:", self.student_id)
        print("Course:", self.course)
        print("GPA:", self.gpa)


class Employee(Person):
    def __init__(self, name, address, weight, height, employee_id, department, salary):
        super().__init__(name, address, weight, height)
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def show(self):
        super().show()
        print("BMI:", round(super().getBMI(), 2))
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Salary:", self.salary)


student = Student("jame", "116/4", 70, 1.72, 6901012610382, "computer engineer", 3.0)
student.show()

print()

employee = Employee("Pepper", "22/1", 65, 1.68, "E404", "IT", 30000)
employee.show()