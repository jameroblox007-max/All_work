def can_fit_volleyball(area):

    return area >= 162

def can_fit_basketball(area):

    return area >= 420

def can_fit_football(area):

    return area >= 7140

def calculate_land_area(width, length):
    area = width * length
    print(f"\n--- ผลการคำนวณพื้นที่ ---")
    print(f"ความกว้าง: {width} เมตร | ความยาว: {length} เมตร")
    print(f"พื้นที่ทั้งหมด: {area:,.2f} ตารางเมตร")
    print("----------------------------")
    print("กีฬาที่สามารถจัดแข่งขันได้ในพื้นที่นี้:")

    has_any_sport = False

    if can_fit_volleyball(area):
        print("- Volleyball (สนามวอลเลย์บอล)")
        has_any_sport = True

    if can_fit_basketball(area):
        print("- Basketball (สนามบาสเกตบอล)")
        has_any_sport = True

    if can_fit_football(area):
        print("- Football (สนามฟุตบอลมาตรฐาน 11 คน)")
        has_any_sport = True

    if not has_any_sport:
        print("- พื้นที่เล็กเกินไป ไม่พอสำหรับสร้างสนามแข่งขันกีฬาที่ระบุข้างต้น")

try:
    w = float(input("กรุณากรอกความกว้างของที่ดิน (เมตร): "))
    l = float(input("กรุณากรอกความยาวของที่ดิน (เมตร): "))

    if w <= 0 or l <= 0:
        print("ความกว้างและความยาวต้องมากกว่า 0")
    else:
        calculate_land_area(w, l)

except ValueError:
    print("ข้อผิดพลาด: กรุณากรอกเฉพาะตัวเลขเท่านั้น")