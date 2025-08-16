num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print("1. Addition")
print("2.Subtraction")
print("3.Multiplcation")
print("4.Division")
User = input("Enter your request (1/2/3/4): ")

def Calculator():
    if User == "1":
        print(num1+num2)
    elif User == "2":
        print(num1-num2)
    elif User == "3":
        print(num1*num2)
    elif User == "4":
        if num2 != 0 :
            print(num1/num2)
        else:
            print("You cannot divide by zero")

# Calculator()


