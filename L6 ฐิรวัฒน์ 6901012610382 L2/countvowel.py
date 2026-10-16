s = input("Enter a string: ")
char = input("Enter a character to count: ")

def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

print("char = ",count_char(s, char))
def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total_vowels = 0
    for v in vowels:
        total_vowels += text.lower().count(v)
    return total_vowels

print("vowels = ",count_vowels(s))