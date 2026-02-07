def find_pairs(arr1, arr2, target):
    set2 = set(arr2)

    result = []
    for item in arr1:
        if target - item in set2:
            result.append((item, target - item))

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)


"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
