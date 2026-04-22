def procces_list(list):
    if not list:
        return []
    
    average = sum(list) / len(list)

    n = len(list)
    one_third = n // 3
    two_thirds = 2 * n // 3

    if average > 0:
        sorted_part = sorted(list[:two_thirds])
        reversed_part = list[two_thirds:][::-1]
        result = sorted_part + reversed_part
    else:
        sorted_part = sorted(list[:one_third])
        reversed_part = list[one_third:][::-1]
        result = sorted_part + reversed_part
    
    return result

test1 = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print(f"Исходный список 1: {test1}")
print(f"Среднее арифметическое: {sum(test1) / len(test1):.1f}")
print(f"Результат: {procces_list(test1)}\n")

    