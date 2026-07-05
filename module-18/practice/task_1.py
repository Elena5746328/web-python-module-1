def conditional_sort(lst):
    if not lst:
        return lst
    
    n = len(lst)
    avg = sum(lst) / n

    two_thirds = (2 * n) // 3
    one_third = n // 3

    if avg > 0:
        sorted_part = sorted(lst[:two_thirds])
        rest_part = lst[two_thirds:]
    else:
        sorted_part = sorted(lst[:one_third])
        rest_part = lst[one_third:]

    rest_part_reversed = rest_part[::-1]

    return sorted_part + rest_part_reversed

data = [5, -2, 3, 8, -1, 4, 7, 2, 6]
result = conditional_sort(data)
print("Исходный список:", data)
print("Результат:", result)