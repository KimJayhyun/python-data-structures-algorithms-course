def group_anagrams(strings: list):
    groups = {}

    for string in strings:
        char_count = {}

        for char in string:
            char_count[char] = char_count.get(char, 0) + 1

        key = tuple(sorted(char_count.items()))

        if key not in groups:
            groups[key] = []
        groups[key].append(string)

    return list(groups.values())


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
