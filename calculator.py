def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def main():
    while True:
        print("\nSimlpe Calculator")
        print("1.Add")
        print("2.Subtract")
        print("3.Exit")

        choice = int(input("Enter your choice: "))
        if choice == 3:
            print("Goodbuy")
            break

        num1 = float(input("Enter first nummber:"))
        num2 = float(input("Enter second number:"))

        if choice == 1:
            print("REsult is ", add(num1, num2))
        
        elif choice == 2:
            print("Result is ",sub(num1, num2))
        
        else:
            print("Envalid number")

if __name__ == "__main__":
    main()