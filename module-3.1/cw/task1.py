# my_list = [1, 2, 3, True]
# print(len(my_list))

# my_list = [[1, 2], [3, 4]]
# length = len(my_list)
# print(length)

# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)

# numbers = [1, 2, 3, 4, 5]
# maximum = max(numbers)
# minimum = min(numbers)
# print(minimum, maximum)

# numbers = [3, 1, 7, 8, 4, 9, 2]
# sorted_nums = sorted(numbers, reverse=True)
# print(sorted_nums)

# numbers = [3, 1, 7, 8, 4, 9, 2]
# reversed_list = reversed(numbers)
# print(list(reversed_list))

# fruits = ["apple", "cherry", "banana"]
# for index, fruit in enumerate(fruits):
#     print(f"{index}: {fruit}")

# def double(num):
#     return num * 2

# numbers = ["1", "2", "3"]
# # s = list(map(lambda x: x**2, numbers))
# s = list(map(int, numbers))

# list_double = list(map(double, s))
# print(list_double)

# def filter_func(num):
#     return num % 2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# evens1 = list(filter(filter_func, numbers))
# print(evens)

# words = ["paper", "apple", "car"]
# result = "-".join(words)
# print(result)

# my_list = ["apple", 2, "ban"]
# my_list_1 = ["banana", 3, "a"]
# new_list = my_list + my_list_1
# my_list += my_list_1
# print(new_list)
# my_list.append(4)
# my_list.extend([5,6])
# print(my_list)

# my_list = ["apple", 2, "ban"]
# my_list.insert(1, "apple")
# my_list.remove("apple")
# my_list.pop()
# my_list.pop(1)
# my_list.clear()
# print(my_list)

# my_list = [5, 2, 8, 4, 2, 2, 7, 2]
# count = my_list.count(2)
# my_list.sort()
# my_list.sort(reverse=True)
# my_list.reverse()
# print(my_list)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# # list[start:end:step]
# print(my_list[::-1])
# print(my_list[-5:])
# print(my_list[-1])
# print(my_list[:])
# print(my_list[2:])
# print(my_list[:6])
# print(my_list[0:5])
# print(my_list[0:5:2])

my_list = [-5,1,2,3,4,5,6,7,8,9,10]
#Краткая запись
# [x**2 for x in my_list]
# [x for x in my_list if x % 2 == 0]
res = [0 if x < 0 else x for x in my_list]
print(res)

#Полная запись
result = []
for x in my_list:
    result.append(x**2)

print(res, result)




