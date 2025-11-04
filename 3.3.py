def split_list(lst):
    if not lst:
        return [[], []]
    mid = (len(lst) + 1) // 2
    a = lst[:mid]
    b = lst[mid:]
    return [a, b]

# Приклади для перевірки
print(split_list([40, -2, 22, 5, 9]))
print(split_list([33, 66, 99]))
print(split_list([1, 2, 3]))
print(split_list([1]))
print(split_list([]))
