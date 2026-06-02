def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "can't divide by zero !"
    else:
     return a/b
    
n1=float(input("enter number 1 : "))
n2=float(input("enter number 2 : "))
while True:
    print("\n..Calculator..")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit..")
    choice=input("enter the choice: ")
    if choice=="5":
        print("Exiting...")
        break
    if choice=="1":
        print("result = ",add(n1,n2))
    elif choice=="2":
        print("result = ",subtract(n1,n2))
    elif choice=="3":
        print("result = ",multiply(n1,n2))
    elif choice=="4":
        print("result = ",div(n1,n2))
    else:
        print("Invalid choice! ")
        break
