def first_non_repeating_char(string):
    hash_table = dict()

    if len(string) == 1:
        return string

    for char in string:
        hash_table[char] = hash_table.get(char, 0) + 1

    for char in string:
        if hash_table[char] == 1:
            return char

    return None


print(first_non_repeating_char("aabc"))
print(first_non_repeating_char("aabbc"))
print(first_non_repeating_char("leetcode"))

print(first_non_repeating_char("hello"))

print(first_non_repeating_char("aabbcc"))


"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
