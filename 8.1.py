def add_one(some_list):
    number_str = ''.join(str(d) for d in some_list)
    number = int(number_str) + 1
    return [int(c) for c in str(number)]
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]
print("ОК")