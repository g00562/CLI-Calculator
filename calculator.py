def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    
    return a / b

def main():
    while True:
        print("\nSimlpe Calculator")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")

        choice = int(input("Enter your choice: "))
        if choice == 5:
            print("Goodbuy")
            break

        num1 = float(input("Enter first nummber:"))
        num2 = float(input("Enter second number:"))

        if choice == 1:
            print("REsult is ", add(num1, num2))
        
        elif choice == 2:
            print("Result is ",sub(num1, num2))
        
        elif choice == 3:
            print("Result is ",multiply(num1, num2))

        elif choice == 4:
            print("Result is ",divide(num1, num2))
        
        else:
            print("Envalid number")

if __name__ == "__main__":
    main()