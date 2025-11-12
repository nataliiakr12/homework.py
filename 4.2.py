def index_sum(lst):
    if not lst:
        return 0
    total = 0
    for index, value in enumerate(lst):
        if index % 2 == 0:
            total += value
    result = total * lst[-1]
    return result

print(index_sum([0, 1, 7, 2, 4, 8]))
print(index_sum([1, 3, 5]))
print(index_sum([6]))
print(index_sum([]))