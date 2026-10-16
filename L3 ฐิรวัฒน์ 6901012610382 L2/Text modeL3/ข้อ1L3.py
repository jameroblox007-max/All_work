def calculate_bmi(weight_kg, height_cm):

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 25.0:
        status = "Healthy Weight"
    elif 25.0 <= bmi < 30.0:
        status = "Overweight"
    else:
        status = "Obesity"
        
    return round(bmi, 1), status

try:
    weight = float(input("ป้อนน้ำหนัก (กิโลกรัม): "))
    height = float(input("ป้อนส่วนสูง (เซนติเมตร): "))
    
    if weight <= 0 or height <= 0:
        print("กรุณากรอกค่าน้ำหนักและส่วนสูงที่มากกว่า 0")
    else:
        bmi_value, weight_status = calculate_bmi(weight, height)
        print(f"\n--- ผลการคำนวณ ---")
        print(f"ค่า BMI: {bmi_value}")
        print(f"สถานะน้ำหนัก: {weight_status}")

except ValueError:
    print("กรุณากรอกตัวเลขที่ถูกต้อง")