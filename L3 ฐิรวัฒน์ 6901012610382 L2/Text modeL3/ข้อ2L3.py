def calculate_grade(score):

    if score < 0 or score > 100:
        return "คะแนนต้องอยู่ระหว่าง 0 ถึง 100 เท่านั้น"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

try:
    user_score = float(input("กรุณากรอกคะแนน (0-100): "))
    result_grade = calculate_grade(user_score)

    print(f"\n--- ผลการตัดเกรด ---")
    print(f"คะแนน: {user_score}")
    print(f"เกรดที่ได้: {result_grade}")

except ValueError:
    print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้น")