s = input("Enter a string: ")
char = input("Enter a character to count: ")

def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print("char = ",count_char(s, char))