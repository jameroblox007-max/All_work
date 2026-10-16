def say_hello(choice):
    if choice == 1:
        print("Hello, KMUTNB")
    elif choice == 2:
        print("Sawasdee, KMUTNB")
    elif choice == 3:
        print("koniciwa, KMUTNB!")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
print("Select a greeting:")
print("1. Hello")
print("2. Sawasdee")
print("3. Koniciwa")
choice = int(input("Enter your choice: "))
say_hello(choice)
