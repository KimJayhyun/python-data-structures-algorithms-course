"""
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.
"""


# O(n^2)
def common1(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False


# O(n)
def item_in_common(list1, list2):
    hash_table = {}

    for item in list1:
        hash_table[item] = True

    for item in list2:
        if item in hash_table:
            return True

    return False
