marks=int(input("enter students score"))
if marks is divisible by 4:
    print("it is a leap year")
elif  marks >60 and marks <=80:
    print("you scored a B")
elif marks > 40 and marks <= 60:
    print("you scored a C")
elif marks > 30 and marks <= 40:
    print("you scored a D")
elif marks > 0 and marks <= 30:
    print("you FAILED")
else :
    print("wrong input")