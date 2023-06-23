def add (x,y):
    return  x+y
def subtract(x,y):
    return  x-y
def divide (x,y):
    return  x/y
def multiply (x,y):
    return  x*y
print ("select operator")
print(" add")
print(" subtract")
print(" divide")
print(" multiply")
choice =input("enter choice add, subtract,divide,multiply")
num1 =int(input("enter first number:"))
num2 =int(input("enter second number:"))

if choice=="add":
    print(num1,"+" , num2 ,"=",add(num1,num2))
elif choice =="subtract":
    print(num1,"-", num2,"=", add(num1,num2))
elif choice=="divide":
    print(num1, "/", num2, "=",divide(num1, num2))
elif choice=="multiply":
    print(num1, "*", num2, "=",multiply(num1, num2))

