s = input("Enter a string: ")
def count_words(text):
    words = text.split()
    return len(words)
print("word =", count_words(s))