numbers = (555, -999, 333, 222, -111, 888, 444, 777, -666, 222, 888, 555)

statistics = {}

for i in numbers:
    num_digits = len(str(abs(i)))
    statistics[num_digits] = statistics.setdefault(num_digits, 0) + 1

for i in sorted(statistics):
    print(i, statistics[i])








    



