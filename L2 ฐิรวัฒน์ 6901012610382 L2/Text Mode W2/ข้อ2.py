def print_roof():    
    print("   ^    ")
    print("  ^  ^  ")
    print(" ^    ^ ")
    print("^      ^")

    
def print_celling():
    print("||||||||")
    
def print_walls():
    print("|      |")
    print("|      |")
    
def print_floor():
    print("||||||||")
    
def print_house(h):
    print_roof()
    
    for _ in range(h):
        print_celling()
        print_walls()
    
    
    print_floor()
    
print("Height of the house: ")
h = int(input())
print_house(h)
