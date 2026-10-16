class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def show_detail(self):
        print(f"รหัส: {self.emp_id} | ชื่อ: {self.name} | เงินเดือน: {self.salary:,.2f} บาท")

    def give_bonus(self, amount):
        self.salary += amount
        print(f" {self.name} ได้รับโบนัสเพิ่ม {amount:,.2f} บาท (เงินเดือนใหม่: {self.salary:,.2f} บาท)")

class Manager(Employee):
    def approve_leave(self, employee_name):
        print(f" ผู้จัดการ {self.name} อนุมัติการลาให้แก่ {employee_name}")

emp1 = Employee("E001", "สมชาย ใจดี", 25000)
mgr = Manager("M001", "หัวหน้าสมศักดิ์", 50000)

emp1.show_detail()
emp1.give_bonus(5000)
print("-" * 40)
mgr.show_detail()
mgr.approve_leave("สมชาย ใจดี")