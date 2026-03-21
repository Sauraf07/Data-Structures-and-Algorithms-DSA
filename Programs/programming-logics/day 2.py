array = [10,25,3,6,4]
sum = 0
for i in array:
    sum += i
    if i % 2 == 0:
        print("Even ",i)
    else:
        print("Odd",i)
array.reverse()
print(array)
print("Total is",sum)
average = sum/len(array)
print("Average is ",average)