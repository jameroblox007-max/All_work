football = int(input("กรุณากรอกจำนวนลูก Football: "))
basketball = int(input("กรุณากรอกจำนวนลูก Basketball: "))
volleyball = int(input("กรุณากรอกจำนวนลูก Volleyball: "))

print("\n--- ผลการเปรียบเทียบ ---")

if football == basketball and basketball == volleyball:
    print(f"กีฬา ทุกชนิด มีจำนวนเท่ากันทั้งหมด คือ {football} ลูก")

elif football >= basketball and football >= volleyball:
    if football == basketball:
        print(f"Football และ Basketball มีจำนวนมากที่สุดเท่ากัน คือ {football} ลูก")
    elif football == volleyball:
        print(f"Football และ Volleyball มีจำนวนมากที่สุดเท่ากัน คือ {football} ลูก")
    else:
        print(f"Football มีจำนวนมากที่สุด คือ {football} ลูก")

elif basketball >= football and basketball >= volleyball:
    if basketball == volleyball:
        print(f"Basketball และ Volleyball มีจำนวนมากที่สุดเท่ากัน คือ {basketball} ลูก")
    else:
        print(f"Basketball มีจำนวนมากที่สุด คือ {basketball} ลูก")

else:
    print(f"Volleyball มีจำนวนมากที่สุด คือ {volleyball} ลูก")