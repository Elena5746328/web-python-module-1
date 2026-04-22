def improved_bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swaps_count = 0

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps_count += 1

        if swaps_count == 0:
            print(f"Сортировка звершена на проходе {i + 1}. Список уже отсортирован")
            break
    
    return arr

test_list = [64< 34, 25, 12, 22, 11, 90, 5]
print(f"исходный список: {test_list}")

sorted_list = improved_bubble_sort(test_list[:])
print(f"Отсортированный список: {sorted_list}")



