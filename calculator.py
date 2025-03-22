def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y==0:
        return "error!"
    return x / y
print("select operation:")
print("1: Add")
print("2: Subtract")
print("3: Multiply")
print("4: Divide")

while True:
    choice  = input("enter choice(1/2/3/4):")

    if choice in ('1','2','3','4'):
        n1=float(input("enter first number"))
        n2=float(input("enter second number"))

        if choice =='1':
          print("result", add(n1, n2))
        elif choice =='2':
          print("result", subtract(n1, n2))
        elif choice == '3':
          print("result", multiply(n1, n2))
        elif choice == '4':
         print("result", divide(n1, n2))

        next_calc=input("do you want to perform another calculation, yes/no")
        if next_calc.lower()!='yes':
            break
    else:
        print("invalid input")
