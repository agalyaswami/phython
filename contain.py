def group_values(data, n):
    for value in data:
        if n == value:
            return True
    return False
print(group_values([1, 5, 8, 3], 3))
print(group_values([5, 8, 3], -1))
