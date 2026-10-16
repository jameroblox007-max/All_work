def is_perfect(n):
    total = 0
    for i in range(1, n):  
        if n % i == 0:      
            total += i       
    return total == n

for num in range(1, 50):
    if is_perfect(num):
        print(num)