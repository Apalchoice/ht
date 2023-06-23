age=int(input("enter age"))
if age == 0 and age <= 5:
    print("ticket is free")
elif age > 6 and age <= 12:
    print("ticket is 500")
elif age > 13 and age <= 17:
    print("ticket is 1000")
elif age >18 :
    print("ticket is 1500")
