def flat1(nested_list):
    flat = []
    for arr in nested_list:
        for element in arr:
            flat.append(element)
    return flat

print(flat1([[1,2,3], [4,5], [6]]))


   