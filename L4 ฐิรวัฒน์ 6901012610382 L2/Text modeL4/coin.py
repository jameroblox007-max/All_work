amount = int(input("Enter amount: "))

while amount != 0:
    coin10 = amount // 10
    remainder = amount % 10
    coin5 = remainder // 5
    remainder = remainder % 5
    coin1 = remainder

    print("เหรียญ 10 จำนวน", coin10, "เหรียญ")
    print("เหรียญ 5 จำนวน", coin5, "เหรียญ")
    print("เหรียญ 1 จำนวน", coin1, "เหรียญ")

    amount = int(input("Enter amount: "))