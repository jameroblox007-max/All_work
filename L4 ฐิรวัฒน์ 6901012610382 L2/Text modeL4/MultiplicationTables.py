def multiplication_table(n):
    i = 1
    while i <= 12:
        print(n, "x", i, "=", n * i)
        i += 1

num = int(input("Enter a number: "))
multiplication_table(num)