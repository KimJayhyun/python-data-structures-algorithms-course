def longest_consecutive_sequence(arr: list):
    given_set = set(arr)

    result = 0
    for item in given_set:
        if item - 1 in given_set:
            continue

        need_to_find = item
        length = 1

        while True:
            need_to_find += 1
            if need_to_find in given_set:
                length += 1
            else:
                break

        result = result if result > length else length

    return result


print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))


"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
