def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average=total/count
    return average

dataset=[4,32,525,54,32,2,]
answer=calculate_average(dataset)
print("the average is",answer)