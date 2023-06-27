def add (x,y):
    return  x+y
def subtract(x,y):
    return  x-y
def divide (x,y):
    return  x/y
def multiply (x,y):
    return  x*y
print ("select operator")
print("a. add")
print("b. subtract")
print("c. divide")
print("d. multiply")
choice =input("enter choice add, subtract,divide,multiply")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))

if choice=="a":
    print(num1,"+" , num2 ,"=",add(num1,num2))
elif choice =="b":
    print(num1,"-", num2,"=", add(num1,num2))
elif choice=="c":
    print(num1, "/", num2, "=",divide(num1, num2))
elif choice=="d":
    print(num1, "*", num2, "=",multiply(num1, num2))

