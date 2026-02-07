def subarray_sum(numbers: list, target):
    if len(numbers) == 0:
        return []

    elif len(numbers) == 1:
        if target == numbers[0]:
            return [0, 0]
        else:
            return []

    sum_index = {0: -1}
    summation = 0

    for idx in range(len(numbers)):
        number = numbers[idx]
        summation += number

        needed_number = summation - target

        if needed_number in sum_index:
            needed_index = sum_index[needed_number]
            return [needed_index + 1, idx]

        sum_index[summation] = idx

    return []


nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
