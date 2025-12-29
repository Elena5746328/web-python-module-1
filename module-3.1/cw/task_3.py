numbers = [0,1,2,3,4,5,6,7,8,9,10]
average = sum(numbers) / len(numbers)
av = [x for x in numbers if x > average]
print(average)
print(av)