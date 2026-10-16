str = input("Enter a string: ")
def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
if is_palindrome(str):
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")